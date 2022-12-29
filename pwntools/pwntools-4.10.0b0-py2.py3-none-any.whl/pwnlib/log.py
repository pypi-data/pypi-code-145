"""
Logging module for printing status during an exploit, and internally
within ``pwntools``.

Exploit Developers
------------------
By using the standard ``from pwn import *``, an object named ``log`` will
be inserted into the global namespace.  You can use this to print out
status messages during exploitation.

For example,::

    log.info('Hello, world!')

prints::

    [*] Hello, world!

Additionally, there are some nifty mechanisms for performing status updates
on a running job (e.g. when brute-forcing).::

    p = log.progress('Working')
    p.status('Reticulating splines')
    time.sleep(1)
    p.success('Got a shell!')


The verbosity of logging can be most easily controlled by setting
``log_level`` on the global ``context`` object.::

    log.info("No you see me")
    context.log_level = 'error'
    log.info("Now you don't")

The purpose of this attribute is to control what gets printed to the screen,
not what gets emitted. This means that you can put all logging events into
a log file, while only wanting to see a small subset of them on your screen.

Pwnlib Developers
-----------------
A module-specific logger can be imported into the module via::

    from pwnlib.log import getLogger
    log = getLogger(__name__)

This provides an easy way to filter logging programmatically
or via a configuration file for debugging.

When using ``progress``, you should use the ``with``
keyword to manage scoping, to ensure the spinner stops if an
exception is thrown.

Technical details
-----------------
Familiarity with the :mod:`logging` module is assumed.

A pwnlib root logger named 'pwnlib' is created and a custom handler and
formatter is installed for it.  The handler determines its logging level from
:data:`context.log_level`.

Ideally :data:`context.log_level` should only affect which records will be
emitted by the handler such that e.g. logging to a file will not be changed by
it. But for performance reasons it is not feasible log everything in the normal
case. In particular there are tight loops inside :mod:`pwnlib.tubes.tube`, which
we would like to be able to debug, but if we are not debugging them, they should
not spit out messages (even to a log file). For this reason there are a few places
inside pwnlib, that will not even emit a record without :data:`context.log_level`
being set to `logging.DEBUG` or below.

Log records created by ``Progress`` and ``Logger`` objects will set
``'pwnlib_msgtype'`` on the ``extra`` field to signal which kind of message was
generated.  This information is used by the formatter to prepend a symbol to the
message, e.g. ``'[+] '`` in ``'[+] got a shell!'``

This field is ignored when using the ``logging`` module's standard formatters.

All status updates (which are not dropped due to throttling) on progress loggers
result in a log record being created.  The ``extra`` field then carries a
reference to the ``Progress`` logger as ``'pwnlib_progress'``.

If the custom handler determines that :data:`term.term_mode` is enabled, log
records that have a ``'pwnlib_progess'`` in their ``extra`` field will not
result in a message being emitted but rather an animated progress line (with a
spinner!) being created.  Note that other handlers will still see a meaningful
log record.

The custom handler will only handle log records whith a level of at least
:data:`context.log_level`.  Thus if e.g. the level for the
``'pwnlib.tubes.ssh'`` is set to ``'DEBUG'`` no additional output will show up
unless :data:`context.log_level` is also set to ``'DEBUG'``.  Other handlers
will however see the extra log records generated by the ``'pwnlib.tubes.ssh'``
logger.
"""
from __future__ import absolute_import
from __future__ import division

import logging
import os
import random
import re
import six
import string
import sys
import threading
import time

from pwnlib import term
from pwnlib.config import register_config
from pwnlib.context import Thread
from pwnlib.context import context
from pwnlib.exception import PwnlibException
from pwnlib.term import spinners
from pwnlib.term import text

__all__ = [
    'getLogger', 'install_default_handler', 'rootlogger'
]



# list of prefixes to use for the different message types.  note that the `text`
# module won't add any escape codes if `pwnlib.context.log_console.isatty()` is `False`
_msgtype_prefixes = {
    'status'       : [text.magenta, 'x'],
    'success'      : [text.bold_green, '+'],
    'failure'      : [text.bold_red, '-'],
    'debug'        : [text.bold_red, 'DEBUG'],
    'info'         : [text.bold_blue, '*'],
    'warning'      : [text.bold_yellow, '!'],
    'error'        : [text.on_red, 'ERROR'],
    'exception'    : [text.on_red, 'ERROR'],
    'critical'     : [text.on_red, 'CRITICAL'],
    'info_once'    : [text.bold_blue, '*'],
    'warning_once' : [text.bold_yellow, '!'],
    }


def read_log_config(settings):
    log = getLogger(__name__)
    for key, value in settings.items():
        if '.' not in key:
            log.warn("Invalid configuration option %r in section %r" % (key, 'log'))
            continue

        msgtype, key = key.split('.', 1)

        if key == 'color':
            current = _msgtype_prefixes[msgtype][0]
            _msgtype_prefixes[msgtype][0] = getattr(text, value, current)

        elif key == 'symbol':
            _msgtype_prefixes[msgtype][1] = value

        else:
            log.warn("Unknown configuration option %r in section %r" % (key, 'log'))

register_config('log', read_log_config)

# the text decoration to use for spinners.  the spinners themselves can be found
# in the `pwnlib.term.spinners` module
_spinner_style = text.bold_blue

class Progress(object):
    """
    Progress logger used to generate log records associated with some running
    job.  Instances can be used as context managers which will automatically
    declare the running job a success upon exit or a failure upon a thrown
    exception.  After :meth:`success` or :meth:`failure` is called the status
    can no longer be updated.

    This class is intended for internal use.  Progress loggers should be created
    using :meth:`Logger.progress`.
    """
    def __init__(self, logger, msg, status, level, args, kwargs):
        self._logger = logger
        self._msg = msg
        self._status = status
        self._level = level
        self._stopped = False
        self.last_status = 0
        self.rate = kwargs.pop('rate', 0)
        self._log(status, args, kwargs, 'status')
        # it is a common use case to create a logger and then immediately update
        # its status line, so we reset `last_status` to accommodate this pattern
        self.last_status = 0

    def _log(self, status, args, kwargs, msgtype):
        # Logs are strings, not bytes.  Handle Python3 bytes() objects.
        status = _need_text(status)

        # this progress logger is stopped, so don't generate any more records
        if self._stopped:
            return
        msg = self._msg
        if msg and status:
            msg += ': '
        msg += status
        self._logger._log(self._level, msg, args, kwargs, msgtype, self)

    def status(self, status, *args, **kwargs):
        """status(status, *args, **kwargs)

        Logs a status update for the running job.

        If the progress logger is animated the status line will be updated in
        place.

        Status updates are throttled at one update per 100ms.
        """
        now = time.time()
        if (now - self.last_status) > self.rate:
            self.last_status = now
            self._log(status, args, kwargs, 'status')

    def success(self, status = 'Done', *args, **kwargs):
        """success(status = 'Done', *args, **kwargs)

        Logs that the running job succeeded.  No further status updates are
        allowed.

        If the Logger is animated, the animation is stopped.
        """
        self._log(status, args, kwargs, 'success')
        self._stopped = True

    def failure(self, status = 'Failed', *args, **kwargs):
        """failure(message)

        Logs that the running job failed.  No further status updates are
        allowed.

        If the Logger is animated, the animation is stopped.
        """
        self._log(status, args, kwargs, 'failure')
        self._stopped = True

    def __enter__(self):
        return self

    def __exit__(self, exc_typ, exc_val, exc_tb):
        # if the progress logger is already stopped these are no-ops
        if exc_typ is None:
            self.success()
        else:
            self.failure()

class Logger(object):
    """
    A class akin to the :class:`logging.LoggerAdapter` class.  All public
    methods defined on :class:`logging.Logger` instances are defined on this
    class.

    Also adds some ``pwnlib`` flavor:

    * :meth:`progress` (alias :meth:`waitfor`)
    * :meth:`success`
    * :meth:`failure`
    * :meth:`indented`
    * :meth:`info_once`
    * :meth:`warning_once` (alias :meth:`warn_once`)

    Adds ``pwnlib``-specific information for coloring, indentation and progress
    logging via log records ``extra`` field.

    Loggers instantiated with :func:`getLogger` will be of this class.
    """
    _one_time_infos    = set()
    _one_time_warnings = set()

    def __init__(self, logger=None):
        if logger is None:
            # This is a minor hack to permit user-defined classes which inherit
            # from a tube (which do not actually reside in the pwnlib library)
            # to receive logging abilities that behave as they would expect from
            # the rest of the library
            module = self.__module__
            if not module.startswith('pwnlib'):
                module = 'pwnlib.' + module
            # - end hack -

            logger_name = '%s.%s.%s' % (module, self.__class__.__name__, id(self))
            logger = logging.getLogger(logger_name)

        self._logger = logger

    def _getlevel(self, levelString):
        if isinstance(levelString, six.integer_types):
            return levelString
        return logging._levelNames[levelString.upper()]

    def _log(self, level, msg, args, kwargs, msgtype, progress = None):
        # Logs are strings, not bytes.  Handle Python3 bytes() objects.
        msg = _need_text(msg)

        extra = kwargs.get('extra', {})
        extra.setdefault('pwnlib_msgtype', msgtype)
        extra.setdefault('pwnlib_progress', progress)
        kwargs['extra'] = extra
        self._logger.log(level, msg, *args, **kwargs)

    def progress(self, message, status = '', *args, **kwargs):
        """progress(message, status = '', *args, level = logging.INFO, **kwargs) -> Progress

        Creates a new progress logger which creates log records with log level
        `level`.

        Progress status can be updated using :meth:`Progress.status` and stopped
        using :meth:`Progress.success` or :meth:`Progress.failure`.

        If `term.term_mode` is enabled the progress logger will be animated.

        The progress manager also functions as a context manager.  Using context
        managers ensures that animations stop even if an exception is raised.

        .. code-block:: python

           with log.progress('Trying something...') as p:
               for i in range(10):
                   p.status("At %i" % i)
                   time.sleep(0.5)
               x = 1/0
        """
        level = self._getlevel(kwargs.pop('level', logging.INFO))
        return Progress(self, message, status, level, args, kwargs)

    def waitfor(self, *args, **kwargs):
        """Alias for :meth:`progress`."""
        return self.progress(*args, **kwargs)

    def indented(self, message, *args, **kwargs):
        """indented(message, *args, level = logging.INFO, **kwargs)

        Log a message but don't put a line prefix on it.

        Arguments:
            level(int): Alternate log level at which to set the indented
                        message.  Defaults to :const:`logging.INFO`.
        """
        level = self._getlevel(kwargs.pop('level', logging.INFO))
        self._log(level, message, args, kwargs, 'indented')

    def success(self, message, *args, **kwargs):
        """success(message, *args, **kwargs)

        Logs a success message.
        """
        self._log(logging.INFO, message, args, kwargs, 'success')

    def failure(self, message, *args, **kwargs):
        """failure(message, *args, **kwargs)

        Logs a failure message.
        """
        self._log(logging.INFO, message, args, kwargs, 'failure')

    def info_once(self, message, *args, **kwargs):
        """info_once(message, *args, **kwargs)

        Logs an info message.  The same message is never printed again.
        """
        m = message % args
        if m not in self._one_time_infos:
            if self.isEnabledFor(logging.INFO):
                self._one_time_infos.add(m)
            self._log(logging.INFO, message, args, kwargs, 'info_once')

    def warning_once(self, message, *args, **kwargs):
        """warning_once(message, *args, **kwargs)

        Logs a warning message.  The same message is never printed again.
        """
        m = message % args
        if m not in self._one_time_warnings:
            if self.isEnabledFor(logging.WARNING):
                self._one_time_warnings.add(m)
            self._log(logging.WARNING, message, args, kwargs, 'warning_once')

    def warn_once(self, *args, **kwargs):
        """Alias for :meth:`warning_once`."""
        return self.warning_once(*args, **kwargs)

    # logging functions also exposed by `logging.Logger`

    def debug(self, message, *args, **kwargs):
        """debug(message, *args, **kwargs)

        Logs a debug message.
        """
        self._log(logging.DEBUG, message, args, kwargs, 'debug')

    def info(self, message, *args, **kwargs):
        """info(message, *args, **kwargs)

        Logs an info message.
        """
        self._log(logging.INFO, message, args, kwargs, 'info')

    def hexdump(self, message, *args, **kwargs):
        # cyclic dependencies FTW!
        # TODO: Move pwnlib.util.fiddling.hexdump into a new module.
        import pwnlib.util.fiddling

        self.info(pwnlib.util.fiddling.hexdump(message, *args, **kwargs))

    def maybe_hexdump(self, message, *args, **kwargs):
        """maybe_hexdump(self, message, *args, **kwargs)

        Logs a message using indented. Repeated single byte is compressed, and
        unprintable message is hexdumped.
        """
        if len(set(message)) == 1 and len(message) > 1:
            self.indented('%r * %#x' % (message[:1], len(message)), *args, **kwargs)
        elif len(message) == 1 or all(c in string.printable.encode() for c in message):
            for line in message.splitlines(True):
                self.indented(repr(line), *args, **kwargs)
        else:
            import pwnlib.util.fiddling
            self.indented(pwnlib.util.fiddling.hexdump(message), *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        """warning(message, *args, **kwargs)

        Logs a warning message.
        """
        self._log(logging.WARNING, message, args, kwargs, 'warning')

    def warn(self, *args, **kwargs):
        """Alias for :meth:`warning`."""
        return self.warning(*args, **kwargs)

    def error(self, message, *args, **kwargs):
        """error(message, *args, **kwargs)

        To be called outside an exception handler.

        Logs an error message, then raises a ``PwnlibException``.
        """
        self._log(logging.ERROR, message, args, kwargs, 'error')
        raise PwnlibException(message % args)

    def exception(self, message, *args, **kwargs):
        """exception(message, *args, **kwargs)

        To be called from an exception handler.

        Logs a error message, then re-raises the current exception.
        """
        kwargs["exc_info"] = 1
        self._log(logging.ERROR, message, args, kwargs, 'exception')
        raise

    def critical(self, message, *args, **kwargs):
        """critical(message, *args, **kwargs)

        Logs a critical message.
        """
        self._log(logging.CRITICAL, message, args, kwargs, 'critical')

    def log(self, level, message, *args, **kwargs):
        """log(level, message, *args, **kwargs)

        Logs a message with log level `level`.  The ``pwnlib`` formatter will
        use the default :mod:`logging` formater to format this message.
        """
        self._log(level, message, args, kwargs, None)

    def isEnabledFor(self, level):
        """isEnabledFor(level) -> bool

        See if the underlying logger is enabled for the specified level.
        """
        effectiveLevel = self._logger.getEffectiveLevel()

        if effectiveLevel == 1:
            effectiveLevel = context.log_level
        return effectiveLevel <= level

    def setLevel(self, level):
        """setLevel(level)

        Set the logging level for the underlying logger.
        """
        with context.local(log_level=level):
            self._logger.setLevel(context.log_level)

    def addHandler(self, handler):
        """addHandler(handler)

        Add the specified handler to the underlying logger.
        """
        self._logger.addHandler(handler)

    def removeHandler(self, handler):
        """removeHandler(handler)

        Remove the specified handler from the underlying logger.
        """
        self._logger.removeHandler(handler)

    @property
    def level(self):
        return self._logger.level
    @level.setter
    def level(self, value):
        with context.local(log_level=value):
            self._logger.level = context.log_level


class Handler(logging.StreamHandler):
    """
    A custom handler class.  This class will report whatever
    :data:`context.log_level` is currently set to as its log level.

    If :data:`term.term_mode` is enabled log records originating from a progress
    logger will not be emitted but rather an animated progress line will be
    created.

    An instance of this handler is added to the ``'pwnlib'`` logger.
    """
    @property
    def stream(self):
        return context.log_console
    @stream.setter
    def stream(self, value):
        pass
    def emit(self, record):
        """
        Emit a log record or create/update an animated progress logger
        depending on whether :data:`term.term_mode` is enabled.
        """
        # We have set the root 'pwnlib' logger to have a logLevel of 1,
        # when logging has been enabled via install_default_handler.
        #
        # If the level is 1, we should only process the record if
        # context.log_level is less than the record's log level.
        #
        # If the level is not 1, somebody else expressly set the log
        # level somewhere on the tree, and we should use that value.
        level = logging.getLogger(record.name).getEffectiveLevel()
        if level == 1:
            level = context.log_level
        if level > record.levelno:
            return

        progress = getattr(record, 'pwnlib_progress', None)

        # if the record originates from a `Progress` object and term handling
        # is enabled we can have animated spinners! so check that
        if progress is None or not term.term_mode:
            super(Handler, self).emit(record)
            return

        # yay, spinners!

        # since we want to be able to update the spinner we overwrite the
        # message type so that the formatter doesn't output a prefix symbol
        msgtype = record.pwnlib_msgtype
        record.pwnlib_msgtype = 'animated'
        msg = "%s\n" % self.format(record)

        # we enrich the `Progress` object to keep track of the spinner
        if not hasattr(progress, '_spinner_handle'):
            spinner_handle = term.output('')
            msg_handle = term.output(msg)
            stop = threading.Event()
            def spin():
                '''Wheeeee!'''
                state = 0
                states = random.choice(spinners.spinners)
                while True:
                    prefix = '[%s] ' % _spinner_style(states[state])
                    spinner_handle.update(prefix)
                    state = (state + 1) % len(states)
                    if stop.wait(0.1):
                        break
            t = Thread(target = spin)
            t.daemon = True
            t.start()
            progress._spinner_handle = spinner_handle
            progress._msg_handle = msg_handle
            progress._stop_event = stop
            progress._spinner_thread = t
        else:
            progress._msg_handle.update(msg)

        # if the message type was not a status message update, then we should
        # stop the spinner
        if msgtype != 'status':
            progress._stop_event.set()
            progress._spinner_thread.join()
            style, symb = _msgtype_prefixes[msgtype]
            prefix = '[%s] ' % style(symb)
            progress._spinner_handle.update(prefix)

class Formatter(logging.Formatter):
    """
    Logging formatter which performs custom formatting for log records
    containing the ``'pwnlib_msgtype'`` attribute.  Other records are formatted
    using the `logging` modules default formatter.

    If ``'pwnlib_msgtype'`` is set, it performs the following actions:

    * A prefix looked up in `_msgtype_prefixes` is prepended to the message.
    * The message is prefixed such that it starts on column four.
    * If the message spans multiple lines they are split, and all subsequent
      lines are indented.

    This formatter is used by the handler installed on the ``'pwnlib'`` logger.
    """

    # Indentation from the left side of the terminal.
    # All log messages will be indented at list this far.
    indent    = '    '

    # Newline, followed by an indent.  Used to wrap multiple lines.
    nlindent  = '\n' + indent

    def format(self, record):
        # use the default formatter to actually format the record
        msg = super(Formatter, self).format(record)

        # then put on a prefix symbol according to the message type

        msgtype = getattr(record, 'pwnlib_msgtype', None)

        # if 'pwnlib_msgtype' is not set (or set to `None`) we just return the
        # message as it is
        if msgtype is None:
            return msg

        if msgtype in _msgtype_prefixes:
            style, symb = _msgtype_prefixes[msgtype]
            prefix = '[%s] ' % style(symb)
        elif msgtype == 'indented':
            prefix = self.indent
        elif msgtype == 'animated':
            # the handler will take care of updating the spinner, so we will
            # not include it here
            prefix = ''
        else:
            # this should never happen
            prefix = '[?] '

        msg = prefix + msg
        msg = self.nlindent.join(msg.splitlines())
        return msg

def _need_text(s):
    # circular import wrapper
    global _need_text
    from pwnlib.util.packing import _need_text
    return _need_text(s, 2)

# we keep a dictionary of loggers such that multiple calls to `getLogger` with
# the same name will return the same logger
def getLogger(name):
    return Logger(logging.getLogger(name))

class LogfileHandler(logging.FileHandler):
    def __init__(self):
        super(LogfileHandler, self).__init__('', delay=1)
    @property
    def stream(self):
        return context.log_file
    @stream.setter
    def stream(self, value):
        pass
    def handle(self, *a, **kw):
        if self.stream.name is not None:
            super(LogfileHandler, self).handle(*a, **kw)

iso_8601 = '%Y-%m-%dT%H:%M:%S'
fmt      = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
log_file = LogfileHandler()
log_file.setFormatter(logging.Formatter(fmt, iso_8601))

#
# The root 'pwnlib' logger is declared here.  To change the target of all
# 'pwntools'-specific logging, only this logger needs to be changed.
#
# Logging cascades upward through the hierarchy,
# so the only point that should ever need to be
# modified is the root 'pwnlib' logger.
#
# For example:
#     map(rootlogger.removeHandler, rootlogger.handlers)
#     logger.addHandler(myCoolPitchingHandler)
#
rootlogger = getLogger('pwnlib')
console   = Handler()
formatter = Formatter()
console.setFormatter(formatter)

def install_default_handler():
    '''install_default_handler()

    Instantiates a :class:`Handler` and :class:`Formatter` and installs them for
    the ``pwnlib`` root logger.  This function is automatically called from when
    importing :mod:`pwn`.
    '''
    logger         = logging.getLogger('pwnlib')

    if console not in logger.handlers:
        logger.addHandler(console)
        logger.addHandler(log_file)

    logger.setLevel(1)
