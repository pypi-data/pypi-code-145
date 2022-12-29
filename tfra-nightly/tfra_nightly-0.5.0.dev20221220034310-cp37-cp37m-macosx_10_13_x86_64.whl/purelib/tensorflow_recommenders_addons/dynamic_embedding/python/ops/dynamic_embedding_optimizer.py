# Copyright 2020 The TensorFlow Recommenders-Addons Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# lint-as: python3
"""patch on optimizers"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
from tensorflow_recommenders_addons.dynamic_embedding.python.ops.dynamic_embedding_creator import KVCreator
import six

from tensorflow_recommenders_addons import dynamic_embedding as de

from tensorflow.keras.optimizers import Optimizer as keras_optimizer
from tensorflow.python.distribute import distribution_strategy_context as distribute_ctx
from tensorflow.python.distribute import reduce_util as ds_reduce_util
from tensorflow.python.eager import context
from tensorflow.python.framework import ops
from tensorflow.python.keras import backend
from tensorflow.python.keras import initializers
from tensorflow.python.keras.optimizer_v2 import optimizer_v2
from tensorflow.python.keras.utils import tf_utils
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import variables
from tensorflow.python.ops import variable_scope
from tensorflow.python.training import optimizer
from tensorflow.python.training import slot_creator
from tensorflow.python.training.tracking import base as trackable


def DynamicEmbeddingOptimizer(self, bp_v2=False, synchronous=False):
  """ An optimizer wrapper to make any TensorFlow optimizer capable of training
  Dynamic Embeddding Variables.

  Args:
    self: a TensorFlow optimizer.
    bp_v2: If True, updating parameters will use updating instead of setting, which solves
      the race condition problem among workers during back-propagation in large-scale
      distributed asynchronous training. Reference: https://www.usenix.org/system/files/osdi20-jiang.pdf
    synchronous: If True, we will use horovod's all-reduce method to merge the dense grad of model parameter, 
      the default reduce method is SUM. For TrainableWrapper's grad, keep same with before.

  Example usage:

    ```python
    optimizer = tfra.dynamic_embedding.DynamicEmbeddingOptimizer(
        tf.train.AdamOptimizer(0.001))
    ```

  Returns:
    The optimizer itself but has ability to train Dynamic Embedding Variables.
  """
  self._bp_v2 = bp_v2
  self._hvd_sync = synchronous

  original_apply_gradients = self.apply_gradients

  def _distributed_apply(distribution, grads_and_vars, name, apply_state):
    """`apply_gradients` using a `DistributionStrategy`."""

    def apply_grad_to_update_var(var, grad):
      """Apply gradient to variable."""
      if isinstance(var, ops.Tensor):
        raise NotImplementedError("Trying to update a Tensor ", var)

      apply_kwargs = {}
      if not isinstance(var, de.TrainableWrapper):
        if isinstance(grad, ops.IndexedSlices):
          if var.constraint is not None:
            raise RuntimeError(
                "Cannot use a constraint function on a sparse variable.")
          if "apply_state" in self._sparse_apply_args:
            apply_kwargs["apply_state"] = apply_state
          return self._resource_apply_sparse_duplicate_indices(
              grad.values, var, grad.indices, **apply_kwargs)

        if "apply_state" in self._dense_apply_args:
          apply_kwargs["apply_state"] = apply_state
        update_op = self._resource_apply_dense(grad, var, **apply_kwargs)
        if var.constraint is not None:
          with ops.control_dependencies([update_op]):
            return var.assign(var.constraint(var))
        else:
          return update_op
      else:
        if not var.params.trainable:
          return control_flow_ops.no_op()

        with ops.colocate_with(None, ignore_existing=True):
          _slots = [self.get_slot(var, _s) for _s in self.get_slot_names()]
          var._track_optimizer_slots(_slots)

          with ops.control_dependencies([grad]):
            if isinstance(var, de.shadow_ops.ShadowVariable):
              v0 = var.read_value(do_prefetch=False)
            else:
              v0 = var.read_value(do_prefetch=not var.params.bp_v2)
            s0 = [_s.read_value() for _s in _slots]
            _before = [v0] + s0

          if isinstance(grad, ops.IndexedSlices):
            if var.constraint is not None:
              raise RuntimeError(
                  "Cannot use a constraint function on a sparse variable.")
            if "apply_state" in self._sparse_apply_args:
              apply_kwargs["apply_state"] = apply_state
            with ops.control_dependencies(_before):
              _apply_op = self._resource_apply_sparse_duplicate_indices(
                  grad.values, var, grad.indices, **apply_kwargs)
            with ops.control_dependencies([_apply_op]):
              _after = control_flow_ops.group(
                  [var.update_op(v0=v0)] +
                  [_s.update_op(v0=s0[si]) for si, _s in enumerate(_slots)])
              return _after

          if "apply_state" in self._dense_apply_args:
            apply_kwargs["apply_state"] = apply_state
          with ops.control_dependencies(_before):
            update_op = self._resource_apply_dense(grad, var, **apply_kwargs)
          if var.constraint is not None:
            with ops.control_dependencies([update_op]):
              return var.assign(var.constraint(var))
          else:
            with ops.control_dependencies([update_op]):
              _after = control_flow_ops.group(
                  [var.update_op(v0=v0)] +
                  [_s.update_op(v0=s0[si]) for si, _s in enumerate(_slots)])
            return _after

    update_ops = []
    with backend.name_scope(name or self._name):
      for grad, var in grads_and_vars:
        scope_name = ("update" if ops.executing_eagerly_outside_functions() else
                      "update_" + var.op.name)
        # Colocate the update with variables to avoid unnecessary communication
        # delays. See b/136304694.
        with backend.name_scope(
            scope_name), distribution.extended.colocate_vars_with(var):
          update_ops.extend(
              distribution.extended.update(var,
                                           apply_grad_to_update_var,
                                           args=(grad,),
                                           group=False))

      any_symbolic = any(
          isinstance(i, ops.Operation) or tf_utils.is_symbolic_tensor(i)
          for i in update_ops)
      if not context.executing_eagerly() or any_symbolic:
        # If the current context is graph mode or any of the update ops are
        # symbolic then the step update should be carried out under a graph
        # context. (eager updates execute immediately)
        with ops._get_graph_from_inputs(update_ops).as_default():  # pylint: disable=protected-access
          with ops.control_dependencies(update_ops):
            return self._iterations.assign_add(1).op

      return self._iterations.assign_add(1)

  def add_slot(var, slot_name, initializer="zeros", shape=None):
    """Add a new slot variable for `var`."""
    if slot_name not in self._slot_names:
      self._slot_names.append(slot_name)
    var_key = optimizer_v2._var_key(var)
    slot_dict = self._slots.setdefault(var_key, {})
    weight = slot_dict.get(slot_name, None)
    if weight is None:
      if isinstance(initializer, six.string_types) or callable(initializer):
        initializer = initializers.get(initializer)
        if isinstance(
            initializer,
            trackable.CheckpointInitialValueCallable) or (shape is not None):
          slot_shape = shape
        else:
          slot_shape = var.shape
        initial_value = functools.partial(initializer,
                                          shape=slot_shape,
                                          dtype=var.dtype)
      else:
        initial_value = initializer
      with self._distribution_strategy_scope():
        strategy = distribute_ctx.get_strategy()
        if not strategy.extended.variable_created_in_scope(var):
          raise ValueError(
              "Trying to create optimizer slot variable under the scope for "
              "tf.distribute.Strategy ({}), which is different from the scope "
              "used for the original variable ({}). Make sure the slot "
              "variables are created under the same strategy scope. This may "
              "happen if you're restoring from a checkpoint outside the scope".
              format(strategy, var))

        with strategy.extended.colocate_vars_with(var):

          if isinstance(var, de.TrainableWrapper):
            weight = de.create_slots(var, initial_value, slot_name,
                                     var._shared_name, self._bp_v2)
          else:
            weight = variables.Variable(
                name="%s/%s" % (
                    var._shared_name,
                    slot_name,
                ),  # pylint: disable=protected-access
                dtype=var.dtype,
                trainable=False,
                initial_value=initial_value,
            )
        backend.track_variable(weight)
        slot_dict[slot_name] = weight
        self._restore_slot_variable(slot_name=slot_name,
                                    variable=var,
                                    slot_variable=weight)
        self._weights.append(weight)
    return weight

  def _get_or_make_slot(var, val, slot_name, op_name):
    """Find or create a slot for a variable.

        Args:
          var: A `Variable` object.
          val: A `Tensor`.  The initial value of the slot.
          slot_name: Name for the slot.
          op_name: Name to use when scoping the Variable that
            needs to be created for the slot.

        Returns:
          A `Variable` object.
        """
    named_slots = self._slot_dict(slot_name)
    if optimizer._var_key(var) not in named_slots:
      if isinstance(var, de.TrainableWrapper):
        new_slot_variable = de.create_slots(var, val, slot_name, op_name,
                                            self._bp_v2)
      else:
        new_slot_variable = slot_creator.create_slot(var, val, op_name)
      self._restore_slot_variable(slot_name=slot_name,
                                  variable=var,
                                  slot_variable=new_slot_variable)
      named_slots[optimizer._var_key(var)] = new_slot_variable
    return named_slots[optimizer._var_key(var)]

  def _get_or_make_slot_with_initializer(var, initializer, shape, dtype,
                                         slot_name, op_name):
    """Find or create a slot for a variable, using an Initializer.

        Args:
          var: A `Variable` object.
          initializer: An `Initializer`.  The initial value of the slot.
          shape: Shape of the initial value of the slot.
          dtype: Type of the value of the slot.
          slot_name: Name for the slot.
          op_name: Name to use when scoping the Variable that
            needs to be created for the slot.

        Returns:
          A `Variable` object.
        """
    named_slots = self._slot_dict(slot_name)
    if optimizer._var_key(var) not in named_slots:
      if isinstance(var, de.TrainableWrapper):
        new_slot_variable = de.create_slots(var, initializer, slot_name,
                                            op_name, self._bp_v2)
      else:
        new_slot_variable = slot_creator.create_slot_with_initializer(
            var, initializer, shape, dtype, op_name)
      self._restore_slot_variable(slot_name=slot_name,
                                  variable=var,
                                  slot_variable=new_slot_variable)
      named_slots[optimizer._var_key(var)] = new_slot_variable
    return named_slots[optimizer._var_key(var)]

  def _zeros_slot(var, slot_name, op_name):
    """Find or create a slot initialized with 0.0.

        Args:
          var: A `Variable` object.
          slot_name: Name for the slot.
          op_name: Name to use when scoping the Variable that
            needs to be created for the slot.

        Returns:
          A `Variable` object.
        """
    named_slots = self._slot_dict(slot_name)
    if optimizer._var_key(var) not in named_slots:
      if isinstance(var, de.TrainableWrapper):
        new_slot_variable = de.create_slots(var, 0.0, slot_name, op_name,
                                            self._bp_v2)
      else:
        new_slot_variable = slot_creator.create_zeros_slot(var, op_name)
      self._restore_slot_variable(slot_name=slot_name,
                                  variable=var,
                                  slot_variable=new_slot_variable)
      named_slots[optimizer._var_key(var)] = new_slot_variable
    return named_slots[optimizer._var_key(var)]

  def apply_gradients(grads_and_vars, global_step=None, name=None):
    """Apply gradients to variables.
    Args:
      grads_and_vars: List of (gradient, variable) pairs as returned by
        compute_gradients().
      global_step: Optional Variable to increment by one after the
        variables have been updated.
      name: Optional name for the returned operation.  Default to the
        name passed to the Optimizer constructor.

    Returns:
      train_op: apply gradients op to be executed by each replica.

    Raises:
      ValueError: If the grads_and_vars is empty.
      ValueError: If global step is not provided, the staleness cannot be
        checked.
    """
    try:
      import horovod.tensorflow as hvd
    except ImportError:
      raise ValueError(
          "Please install Horovod first if you want to use distributed synchronous training based on Horovod"
      )
    if not grads_and_vars:
      raise ValueError("Must supply at least one variable")

    if global_step is None:
      raise ValueError("Global step is required to check staleness")

    trainable_grad_and_vars = []
    aggregated_grad = []
    var_list = []

    with backend.name_scope(name or self._name):
      for grad, var in grads_and_vars:
        if isinstance(var, de.TrainableWrapper):
          trainable_grad_and_vars.append((grad, var))
          continue
        var_list.append(var)
        with ops.device(var.device):
          # Dense gradients.
          if grad is None:
            aggregated_grad.append(None)  # pass-through.
            continue
          else:
            aggregated_grad.append(hvd.allreduce(grad, op=hvd.Sum))

      aggregated_grads_and_vars = zip(aggregated_grad, var_list)
      update_op = original_apply_gradients(aggregated_grads_and_vars,
                                           global_step)
      if trainable_grad_and_vars:
        trainable_update_op = original_apply_gradients(trainable_grad_and_vars,
                                                       global_step)
        train_op = control_flow_ops.group([update_op, trainable_update_op])
      else:
        train_op = update_op
      return train_op

  if isinstance(self, optimizer.Optimizer):
    self._get_or_make_slot = _get_or_make_slot
    self._get_or_make_slot_with_initializer = _get_or_make_slot_with_initializer
    self._zeros_slot = _zeros_slot
    if self._hvd_sync:
      self.apply_gradients = apply_gradients
  elif isinstance(self, optimizer_v2.OptimizerV2) or isinstance(
      self, keras_optimizer):
    if self._hvd_sync:
      raise Exception(
          "OptimizerV2 didn't support distributed sync train now, please use tf.train.XxxxOptimizer."
      )
    self.add_slot = add_slot
    self._distributed_apply = _distributed_apply
  else:
    raise Exception("Optimizer type is not supported! got {}".format(
        str(type(self))))
  return self


def create_slots(primary, init, slot_name, op_name, bp_v2):
  """Helper function for creating a slot variable for statefull optimizers."""
  params_var_, params_ids_ = primary.params, primary.ids

  scope_store = variable_scope._get_default_variable_store()
  full_name = params_var_.name + "/" + op_name + "/" + slot_name
  if full_name not in scope_store._vars:
    with ops.colocate_with(primary, ignore_existing=True):
      slot_variable_ = de.Variable(
          name=full_name,
          key_dtype=params_var_.key_dtype,
          value_dtype=params_var_.value_dtype,
          dim=params_var_.dim,
          devices=params_var_.devices,
          partitioner=params_var_.partition_fn,
          initializer=init,
          init_size=params_var_.init_size,
          kv_creator=params_var_.kv_creator,
          trainable=False,
          checkpoint=params_var_.checkpoint,
          bp_v2=bp_v2 if bp_v2 is not None else params_var_.bp_v2,
      )

    scope_store._vars[full_name] = slot_variable_
    # Record the optimizer Variable into trace.
    primary._optimizer_vars.append(slot_variable_)

  slot_trainable = None
  if context.executing_eagerly():
    slot_tw_name = slot_name + '-' + str(optimizer_v2._var_key(primary))
  else:
    # In graph mode of former version, It only uses slot_name as name to
    # trainable wrappers of slots. So here set it the name to slot_name
    # for forward compatibility.
    slot_tw_name = slot_name
  if isinstance(primary, de.shadow_ops.ShadowVariable):
    slot_trainable = de.shadow_ops.ShadowVariable(
        params=scope_store._vars[full_name],
        ids=primary.ids,
        exists=primary.exists,
        name=full_name,
        trainable=False,
    )
  else:
    _, slot_trainable = de.embedding_lookup(
        params=scope_store._vars[full_name],
        ids=params_ids_,
        name=slot_tw_name,
        return_trainable=True,
    )

  return slot_trainable
