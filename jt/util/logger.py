from enum import Enum


class LogPriority(Enum):
    info = 'INFO'
    error = 'ERROR'


def _log_message(priority, message):
    print('[{}] {}'.format(priority.value, message))


def info(message):
    _log_message(LogPriority.info, message)


def error(message):
    _log_message(LogPriority.error, message)

