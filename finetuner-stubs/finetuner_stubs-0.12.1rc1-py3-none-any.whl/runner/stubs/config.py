import dataclasses
import inspect
import warnings
from collections import defaultdict
from typing import Any, Dict, List, Literal, Optional, Tuple

from pydantic import BaseModel, Field, confloat, conint, constr, create_model, validator

from _finetuner.runner.stubs import callback, model


def _get_contained_classes(
    package: Any,
    subtype: Any = object,
    subtypes_only: bool = False,
    dataclasses_only: bool = False,
) -> Dict[str, Any]:
    """Search a package for defined classes."""

    def classfilter(cls) -> bool:
        if inspect.isclass(cls) and not inspect.isabstract(cls):
            if subtypes_only:
                if issubclass(cls, subtype):
                    return True
                return False
            if dataclasses_only:
                if dataclasses.is_dataclass(cls):
                    return True
                return False
            return True
        return False

    return {
        name: obj
        for name, obj in inspect.getmembers(package, inspect.isclass)
        if classfilter(obj)
    }


def _get_class_names_and_args(
    package: Any,
    subtype: Any = object,
    subtypes_only: bool = False,
    dataclasses_only: bool = False,
    exclude_args: Tuple[str, ...] = (),
    name_attr: str = '__name__',
) -> Tuple[Tuple[str, ...], Dict[str, BaseModel]]:

    names = set()
    options = {}

    for _, obj in _get_contained_classes(
        package, subtype, subtypes_only, dataclasses_only
    ).items():
        name = str(getattr(obj, name_attr))
        names.add(name)
        _args = {}
        for _, v in inspect.signature(obj).parameters.items():
            if v.name in exclude_args or v.annotation == v.empty:
                continue
            _args[v.name] = (
                (v.annotation, ...)
                if v.empty == v.default
                else (v.annotation, v.default)
            )
        _pyd_model = create_model(f'{obj.__name__}Options', **_args)
        options[name] = _pyd_model

    return tuple(names), options


def _get_tasks_and_models() -> Dict[str, List[str]]:
    """Get a mapping of tasks to models."""
    _model_classes: Dict[str, model._ModelStub] = _get_contained_classes(
        package=model,
        subtype=model._ModelStub,
        subtypes_only=True,
    )
    _tasks2models = defaultdict(list)
    for _, obj in _model_classes.items():
        _tasks2models[obj.task].append(obj.descriptor)

    return _tasks2models


def _get_literals() -> Dict[str, Tuple[Tuple[str, ...], Dict[str, BaseModel]]]:

    _models, _model_options = _get_class_names_and_args(
        model,
        subtype=model._ModelStub,
        subtypes_only=True,
        exclude_args=('preprocess_options', 'collate_options'),
        name_attr='descriptor',
    )
    _callbacks, _callback_options = _get_class_names_and_args(
        callback, dataclasses_only=True
    )
    _literals = {
        'models': (_models, _model_options),
        'callbacks': (_callbacks, _callback_options),
        'losses': (tuple(), {}),
        'miners': (tuple(), {}),
        'optimizers': (tuple(), {}),
    }

    try:
        import torch
        from pytorch_metric_learning.losses import BaseMetricLossFunction
        from pytorch_metric_learning.miners import BaseMiner

        from finetuner import loss, miner

        _literals['losses'] = _get_class_names_and_args(
            loss, subtypes_only=True, subtype=BaseMetricLossFunction
        )
        _literals['miners'] = _get_class_names_and_args(
            miner, subtypes_only=True, subtype=BaseMiner
        )
        _literals['optimizers'] = _get_class_names_and_args(
            torch.optim, subtypes_only=True, subtype=torch.optim.Optimizer
        )
    except (ImportError, ModuleNotFoundError):
        pass

    return _literals


def _get_json_schema_conditions(
    name_arg: str,
    options_arg: str,
    options: Dict[str, BaseModel],
) -> List[Dict[str, Any]]:
    return [
        {
            'if': {'properties': {name_arg: {'const': key}}},
            'then': {'properties': {options_arg: value.schema()}},
        }
        for key, value in options.items()
    ]


tasks2models = _get_tasks_and_models()
literals = _get_literals()
models, model_options = literals['models']
callbacks, callback_options = literals['callbacks']
losses, loss_options = literals['losses']
miners, miner_options = literals['miners']
optimizers, optimizer_options = literals['optimizers']

ModelType = Literal[models] if len(models) > 0 else constr(min_length=1)
CallbackType = Literal[callbacks] if len(callbacks) > 0 else constr(min_length=1)
LossType = Literal[losses] if len(losses) > 0 else constr(min_length=1)
MinerType = Literal[miners] if len(miners) > 0 else Optional[constr(min_length=1)]
OptimizerType = Literal[optimizers] if len(optimizers) > 0 else constr(min_length=1)


class ModelConfig(BaseModel):
    name: ModelType = Field(
        description='The name of the backbone model that will be fine-tuned.'
    )
    freeze: bool = Field(
        default=False,
        description=(
            'If set to True all layers in the backbone model except the last '
            'one will be freezed.'
        ),
    )
    output_dim: Optional[conint(gt=0)] = Field(
        default=None,
        description=(
            'The embedding model\'s output dimensionality. If set, a projection '
            'head will be attached to the backbone model.'
        ),
    )
    options: Dict[str, Any] = Field(
        default_factory=lambda: {},
        description=(
            'Additional arguments to pass to the backbone model construction. These '
            'are model specific options and are different depending on the model you '
            'choose.'
        ),
    )
    to_onnx: bool = Field(
        default=False, description='If set `True` will convert model as onnx.'
    )

    @validator('to_onnx')
    def valid_to_onnx(cls, v_to_onnx, values):
        stubs_dict = model.get_model_stubs_dict()
        v_name = values['name']
        if v_name in stubs_dict:
            if v_to_onnx:
                for c in stubs_dict[v_name]:
                    if not c.supports_onnx_export:
                        raise ValueError(
                            f'The backbone {v_name} mentioned in the config does not '
                            'support ONNX export. Thus you need to set to_onnx=False.'
                        )
        return v_to_onnx

    class Config:

        validate_assignment = True

        @staticmethod
        def schema_extra(schema: Dict[str, Any], *_, **__) -> None:
            conditions = _get_json_schema_conditions(
                name_arg='name', options_arg='options', options=model_options
            )
            if len(conditions) > 0:
                schema['allOf'] = conditions


class DataConfig(BaseModel):
    train_data: constr(min_length=1) = Field(
        description='The training data to use for fine-tuning the model.'
    )
    eval_data: Optional[constr(min_length=1)] = Field(
        default=None,
        description=(
            'Optional evaluation data to use for the fine-tuning run. '
            'Validation loss is computed per epoch agaist this dataset.'
        ),
    )
    val_split: confloat(ge=0, lt=1) = Field(
        default=0.0,
        description=(
            'Determines which portion of the `train_data` specified in the '
            '`fit` function is held out and used for validation (and not for '
            'training). If it is set to 0, or an `eval_data` parameter is provided '
            'to the `fit` function, no training data is held out for validation.'
        ),
    )
    num_workers: conint(gt=0) = Field(
        default=8, description='Number of workers used by the dataloaders.'
    )
    num_items_per_class: conint(gt=1) = Field(
        default=4,
        description='Number of same-class items that will make it in the batch.',
    )

    class Config:
        validate_assignment = True


class CallbackConfig(BaseModel):
    name: CallbackType = Field(description='The name of the callback.')
    options: Dict[str, Any] = Field(
        default_factory=lambda: {},
        description='Arguments to pass to the callback construction.',
    )

    class Config:

        validate_assignment = True

        @staticmethod
        def schema_extra(schema: Dict[str, Any], *_, **__) -> None:
            conditions = _get_json_schema_conditions(
                name_arg='name', options_arg='options', options=callback_options
            )
            if len(conditions) > 0:
                schema['allOf'] = conditions


class HyperParametersConfig(BaseModel):
    optimizer: OptimizerType = Field(
        default='Adam',
        description=(
            'Name of the optimizer that will be used for fine-tuning. See '
            'https://pytorch.org/docs/stable/optim.html for available options.'
        ),
    )
    optimizer_options: Dict[str, Any] = Field(
        default_factory=lambda: {},
        description='Specify arguments to pass to the optimizer construction.',
    )
    loss: LossType = Field(
        default='TripletMarginLoss',
        description=(
            'Name of the loss function to use for fine-tuning. See '
            'https://finetuner.jina.ai/api/finetuner/#finetuner.fit for '
            'available options.'
        ),
    )
    loss_options: Dict[str, Any] = Field(
        default_factory=lambda: {},
        description='Specify arguments to pass to the loss construction.',
    )
    miner: MinerType = Field(
        default=None,
        description=(
            'Specify the miner that will be used for fine-tuning. See '
            'https://kevinmusgrave.github.io/pytorch-metric-learning/miners/ for '
            'available options.'
        ),
    )
    miner_options: Dict[str, Any] = Field(
        default_factory=lambda: {},
        description=(
            'Specify arguments to pass to the miner construction. See '
            'https://kevinmusgrave.github.io/pytorch-metric-learning/miners/ for '
            'detailed information about all possible attributes.'
        ),
    )
    batch_size: conint(gt=0) = Field(
        default=128, description='The training batch size.'
    )
    learning_rate: Optional[confloat(ge=0, lt=1)] = Field(
        default=None,
        description=(
            'The learning rate to use during training. If given, this argument '
            'overwrites the optimizer default learning rate or the learning rate '
            'specified in the optimizer options.'
        ),
    )
    epochs: conint(ge=0, lt=50) = Field(
        default=10, description='Number of fine-tuning epochs.'
    )
    scheduler_step: Literal['batch', 'epoch'] = Field(
        default='batch',
        description=(
            'At which interval should the learning rate scheduler\'s '
            'step function be called. Valid options are `batch` and `epoch`.'
        ),
    )

    @validator('batch_size')
    def batch_size_warning(cls, v):
        if v >= 256:
            warnings.warn('batch_size >= 256 may result in OOM (out of memory) errors.')
        return v

    class Config:

        validate_assignment = True

        @staticmethod
        def schema_extra(schema: Dict[str, Any], *_, **__) -> None:
            optimizer_conditions = _get_json_schema_conditions(
                name_arg='optimizer',
                options_arg='optimizer_options',
                options=optimizer_options,
            )
            loss_conditions = _get_json_schema_conditions(
                name_arg='loss', options_arg='loss_options', options=loss_options
            )
            miner_conditions = _get_json_schema_conditions(
                name_arg='miner', options_arg='miner_options', options=miner_options
            )
            conditions = optimizer_conditions + loss_conditions + miner_conditions
            if len(conditions) > 0:
                schema['allOf'] = conditions


class RunConfig(BaseModel):
    model: ModelConfig = Field(description='Model configuration.')
    data: DataConfig = Field(description='Data configuration.')
    callbacks: List[CallbackConfig] = Field(
        default_factory=lambda: [],
        description='List of callbacks that will be used during fine-tuning.',
    )
    hyper_parameters: HyperParametersConfig = Field(
        default=HyperParametersConfig(), description='Hyper-parameter configuration.'
    )
    public: bool = Field(
        default=False,
        description='If set to True artifact will be set as public artifact.',
    )
    run_name: Optional[constr(min_length=1)] = Field(
        default=None, description='Specify a run name.'
    )
    experiment_name: Optional[constr(min_length=1)] = Field(
        default=None, description='Specify an experiment name.'
    )


__FINETUNER_RUNNER_MODELS__ = tasks2models
__FINETUNER_RUNNER_CONFIG_JSONSCHEMA__ = RunConfig.schema()
__FINETUNER_RUNNER_CONFIG_DATAPATHS__ = [
    'data.train_data',
    'data.eval_data',
    'callbacks.ANY.options.query_data',
    'callbacks.ANY.options.index_data',
]
__FINETUNER_RUNNER_METADATA__ = {
    'models': __FINETUNER_RUNNER_MODELS__,
    'schema': __FINETUNER_RUNNER_CONFIG_JSONSCHEMA__,
    'datapaths': __FINETUNER_RUNNER_CONFIG_DATAPATHS__,
}
