# -*- coding: utf-8 -*-
"""
    salt.log
    ~~~~~~~~


    :copyright: © 2011 UfSoft.org - :email:`Pedro Algarvio (pedro@algarvio.me)`
    :license: BSD, see LICENSE for more details.
"""

import logging

LOG_LEVELS = {
    "none": logging.NOTSET,
    "info": logging.INFO,
    "warn": logging.WARNING,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "none": logging.CRITICAL,
    "debug": logging.DEBUG,
    "trace": 5,
    "garbage": 1
}

LoggingLoggerClass = logging.getLoggerClass()


class Logging(LoggingLoggerClass):
    def garbage(self, msg, *args, **kwargs):
        return LoggingLoggerClass.log(self, 1, msg, *args, **kwargs)

    def trace(self, msg, *args, **kwargs):
        return LoggingLoggerClass.log(self, 5, msg, *args, **kwargs)


def setup_console_logger(log_level):
    import logging
    if logging.getLoggerClass() is not Logging:
        logging.setLoggerClass(Logging)
        logging.addLevelName(5, 'TRACE')
        logging.addLevelName(1, 'GARBAGE')
        # Set the root logger at the lowest level possible
        logging.getLogger().setLevel(1)

    level = LOG_LEVELS.get(log_level.lower(), logging.ERROR)

    rootLogger = logging.getLogger()
    handler = logging.StreamHandler()

    handler.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)03.0f [%(name)-15s][%(levelname)-8s] %(message)s',
        datefmt="%H:%M:%S"
    )

    handler.setFormatter(formatter)
    rootLogger.addHandler(handler)


def setup_logfile_logger(log_path, log_level):
    import logging
    if logging.getLoggerClass() is not Logging:
        logging.setLoggerClass(Logging)
        logging.addLevelName(5, 'TRACE')
        logging.addLevelName(1, 'GARBAGE')
        # Set the root logger at the lowest level possible
        logging.getLogger().setLevel(1)


    level = LOG_LEVELS.get(log_level.lower(), logging.ERROR)

    rootLogger = logging.getLogger()
    import logging.handlers
    handler = getattr(
        logging.handlers, 'WatchedFileHandler', logging.FileHandler)(
            log_path, 'a', 'utf-8', delay=0
    )

    handler.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-15s][%(levelname)-8s] %(message)s',
    )

    handler.setFormatter(formatter)
    rootLogger.addHandler(handler)
