# AUTOGENERATED! DO NOT EDIT! File to edit: ../notebooks/Logger.ipynb.

# %% auto 0
__all__ = ['should_supress_timestamps', 'supress_timestamps', 'get_logger', 'set_level']

# %% ../notebooks/Logger.ipynb 2
from typing import *
import logging

# %% ../notebooks/Logger.ipynb 3
import logging.config
from typer import echo

# %% ../notebooks/Logger.ipynb 4
logging_level = logging.WARNING

# %% ../notebooks/Logger.ipynb 6
# Logger Levels
# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10
# NOTSET = 0

# Create a custom logger and set the configuration to echo the logging messages
# Reference: https://github.com/tiangolo/typer/issues/203


class CLILoggerHandler(logging.Handler):
    """A custom logger handler class that use Typer echo to log results."""

    def emit(self, record: logging.LogRecord) -> None:
        """A function to channel logger outout to Typer echo."""

        echo(self.format(record))


# Global handler for the loggers
handler = CLILoggerHandler()

# %% ../notebooks/Logger.ipynb 7
should_supress_timestamps: bool = False


def supress_timestamps(flag: bool = True):
    global should_supress_timestamps
    should_supress_timestamps = flag


def get_logger(name: str) -> logging.Logger:
    """An internal function to set the default logger configuration

    Returns:
        An instance of Logger with custom configuration that can be used across the CLI for logging
    """

    # Logger Configuration

    global should_supress_timestamps

    if should_supress_timestamps:
        fmt = "[%(levelname)s] %(name)s: %(message)s"
    else:
        fmt = "%(asctime)s.%(msecs)03d [%(levelname)s] %(name)s: %(message)s"

    datefmt = "%y-%m-%d %H:%M:%S"

    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger

# %% ../notebooks/Logger.ipynb 9
def set_level(level: int):

    # Getting all loggers that has either airt or __main__ in the name
    loggers = [
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if ("airt" in name) or ("__main__" in name)
    ]

    for logger in loggers:
        logger.setLevel(level)
