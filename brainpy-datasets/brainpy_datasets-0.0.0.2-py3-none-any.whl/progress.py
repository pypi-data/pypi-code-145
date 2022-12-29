# -*- coding: utf-8 -*-

"""
This file is rewritten from the keras (https://github.com/keras-team/keras).
"""
import os
import sys
import time

import numpy as np

from . import io_utils

__all__ = [
  'Progbar'
]


class Progbar(object):
  """Displays a progress bar.

  Args:
      target: Total number of steps expected, None if unknown.
      width: Progress bar width on screen.
      verbose: Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose)
      stateful_metrics: Iterable of string names of metrics that should *not* be
        averaged over time. Metrics in this list will be displayed as-is. All
        others will be averaged by the progbar before display.
      interval: Minimum visual progress update interval (in seconds).
      unit_name: Display name for step counts (usually "step" or "sample").
  """

  def __init__(
      self,
      target,
      width=30,
      verbose=1,
      interval=0.05,
      stateful_metrics=None,
      unit_name='step'
  ):
    self.target = target
    self.width = width
    self.verbose = verbose
    self.interval = interval
    self.unit_name = unit_name
    if stateful_metrics:
      self.stateful_metrics = set(stateful_metrics)
    else:
      self.stateful_metrics = set()

    self._dynamic_display = ((hasattr(sys.stdout, 'isatty') and
                              sys.stdout.isatty()) or
                             'ipykernel' in sys.modules or
                             'posix' in sys.modules or
                             'PYCHARM_HOSTED' in os.environ)
    self._total_width = 0
    self._seen_so_far = 0
    # We use a dict + list to avoid garbage collection
    # issues found in OrderedDict
    self._values = {}
    self._values_order = []
    self._start = time.time()
    self._last_update = 0
    self._time_at_epoch_start = self._start
    self._time_at_epoch_end = None
    self._time_after_first_step = None

  def update(self, current, values=None, finalize=None):
    """Updates the progress bar.

    Args:
        current: Index of current step.
        values: List of tuples: `(name, value_for_last_step)`. If `name` is in
          `stateful_metrics`, `value_for_last_step` will be displayed as-is.
          Else, an average of the metric over time will be displayed.
        finalize: Whether this is the last update for the progress bar. If
          `None`, defaults to `current >= self.target`.
    """
    if finalize is None:
      if self.target is None:
        finalize = False
      else:
        finalize = current >= self.target

    values = values or []
    for k, v in values:
      if k not in self._values_order:
        self._values_order.append(k)
      if k not in self.stateful_metrics:
        # In the case that progress bar doesn't have a target value in the first
        # epoch, both on_batch_end and on_epoch_end will be called, which will
        # cause 'current' and 'self._seen_so_far' to have the same value. Force
        # the minimal value to 1 here, otherwise stateful_metric will be 0s.
        value_base = max(current - self._seen_so_far, 1)
        if k not in self._values:
          self._values[k] = [v * value_base, value_base]
        else:
          self._values[k][0] += v * value_base
          self._values[k][1] += value_base
      else:
        # Stateful metrics output a numeric value. This representation
        # means "take an average from a single value" but keeps the
        # numeric formatting.
        self._values[k] = [v, 1]
    self._seen_so_far = current

    message = ''
    now = time.time()
    info = ' - %.0fs' % (now - self._start)
    if current == self.target:
      self._time_at_epoch_end = now
    if self.verbose == 1:
      if now - self._last_update < self.interval and not finalize:
        return

      prev_total_width = self._total_width
      if self._dynamic_display:
        message += '\b' * prev_total_width
        message += '\r'
      else:
        message += '\n'

      if self.target is not None:
        numdigits = int(np.log10(self.target)) + 1
        bar = ('%' + str(numdigits) + 'd/%d [') % (current, self.target)
        prog = float(current) / self.target
        prog_width = int(self.width * prog)
        if prog_width > 0:
          bar += ('=' * (prog_width - 1))
          if current < self.target:
            bar += '>'
          else:
            bar += '='
        bar += ('.' * (self.width - prog_width))
        bar += ']'
      else:
        bar = '%7d/Unknown' % current

      self._total_width = len(bar)
      message += bar

      time_per_unit = self._estimate_step_duration(current, now)

      if self.target is None or finalize:
        info += self._format_time(time_per_unit, self.unit_name)
      else:
        eta = time_per_unit * (self.target - current)
        if eta > 3600:
          eta_format = '%d:%02d:%02d' % (eta // 3600,
                                         (eta % 3600) // 60, eta % 60)
        elif eta > 60:
          eta_format = '%d:%02d' % (eta // 60, eta % 60)
        else:
          eta_format = '%ds' % eta

        info = ' - ETA: %s' % eta_format

      for k in self._values_order:
        info += ' - %s:' % k
        if isinstance(self._values[k], list):
          avg = np.mean(self._values[k][0] / max(1, self._values[k][1]))
          if abs(avg) > 1e-3:
            info += ' %.4f' % avg
          else:
            info += ' %.4e' % avg
        else:
          info += ' %s' % self._values[k]

      self._total_width += len(info)
      if prev_total_width > self._total_width:
        info += (' ' * (prev_total_width - self._total_width))

      if finalize:
        info += '\n'

      message += info
      io_utils.print_msg(message, line_break=False)
      message = ''

    elif self.verbose == 2:
      if finalize:
        numdigits = int(np.log10(self.target)) + 1
        count = ('%' + str(numdigits) + 'd/%d') % (current, self.target)
        info = count + info
        for k in self._values_order:
          info += ' - %s:' % k
          avg = np.mean(self._values[k][0] / max(1, self._values[k][1]))
          if avg > 1e-3:
            info += ' %.4f' % avg
          else:
            info += ' %.4e' % avg
        if self._time_at_epoch_end:
          time_per_epoch = self._time_at_epoch_end - self._time_at_epoch_start
          avg_time_per_step = time_per_epoch / self.target
          self._time_at_epoch_start = now
          self._time_at_epoch_end = None
          info += ' -' + self._format_time(time_per_epoch, 'epoch')
          info += ' -' + self._format_time(avg_time_per_step, self.unit_name)
          info += '\n'
        message += info
        io_utils.print_msg(message, line_break=False)
        message = ''

    self._last_update = now

  def add(self, n, values=None):
    self.update(self._seen_so_far + n, values)

  def _format_time(self, time_per_unit, unit_name):
    """format a given duration to display to the user.

    Given the duration, this function formats it in either milliseconds
    or seconds and displays the unit (i.e. ms/step or s/epoch)
    Args:
      time_per_unit: the duration to display
      unit_name: the name of the unit to display
    Returns:
      a string with the correctly formatted duration and units
    """
    formatted = ''
    if time_per_unit >= 1 or time_per_unit == 0:
      formatted += ' %.0fs/%s' % (time_per_unit, unit_name)
    elif time_per_unit >= 1e-3:
      formatted += ' %.0fms/%s' % (time_per_unit * 1e3, unit_name)
    else:
      formatted += ' %.0fus/%s' % (time_per_unit * 1e6, unit_name)
    return formatted

  def _estimate_step_duration(self, current, now):
    """Estimate the duration of a single step.

    Given the step number `current` and the corresponding time `now`
    this function returns an estimate for how long a single step
    takes. If this is called before one step has been completed
    (i.e. `current == 0`) then zero is given as an estimate. The duration
    estimate ignores the duration of the (assumed to be non-representative)
    first step for estimates when more steps are available (i.e. `current>1`).
    Args:
      current: Index of current step.
      now: The current time.
    Returns: Estimate of the duration of a single step.
    """
    if current:
      # there are a few special scenarios here:
      # 1) somebody is calling the progress bar without ever supplying step 1
      # 2) somebody is calling the progress bar and supplies step one multiple
      #    times, e.g. as part of a finalizing call
      # in these cases, we just fall back to the simple calculation
      if self._time_after_first_step is not None and current > 1:
        time_per_unit = (now - self._time_after_first_step) / (current - 1)
      else:
        time_per_unit = (now - self._start) / current

      if current == 1:
        self._time_after_first_step = now
      return time_per_unit
    else:
      return 0

  def _update_stateful_metrics(self, stateful_metrics):
    self.stateful_metrics = self.stateful_metrics.union(stateful_metrics)
