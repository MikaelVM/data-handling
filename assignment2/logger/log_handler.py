"""Module for logging messages to files based on log levels."""

from datetime import datetime
from enum import Enum
from pathlib import Path

from helper_functions import FileHandler


class LogLevel(Enum):
    """Enum representing log levels.

    Attributes:
        INFO: Represents informational messages, mainly used for debugging and tracking the flow of the application.
        WARNING: Represents warning messages, indicating potential issues or situations that may require attention but
            do not necessarily indicate an error.
        ERROR: Represents error messages, indicating that something has gone wrong and may require immediate
            attention or intervention.
    """

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class LogHandler:
    """Class responsible for handling log messages and writing them to files based on log levels."""

    def __init__(self, log_folder_path: Path):
        """Initialize the LogHandler with a specified log folder path.

        Args:
            log_folder_path: The path to the folder where log files will be stored.
        """
        self.log_folder_path = log_folder_path

    def log(self, message: str, level: LogLevel) -> None:
        """Log a message to a file based on the log level.

        Args:
            message: The message to be logged.
            level: The log level indicating the severity of the message.
        """
        log_file_path = self.log_folder_path / self._log_file_name(level)
        file_handler = FileHandler(log_file_path)
        message = file_handler.read_file() + self._log_message(message) if log_file_path.exists() \
            else self._log_message(message)

        file_handler.write_to_file(message)

    def clear_logs(self) -> None:
        """Delete all log files in the log folder."""
        for level in LogLevel:
            log_file_path = self.log_folder_path / self._log_file_name(level)
            log_file_path.unlink()

    @staticmethod
    def _log_file_name(level: LogLevel) -> str:
        """Return the file name for a given log level.

        Args:
            level: The log level for which to generate the file name.
        """
        return f"log_{level.value}.txt"

    @staticmethod
    def _log_message(message: str) -> str:
        """Format a log message with a timestamp.

        Args:
            message: The message to be formatted.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
        return f"{timestamp}: \n{message}\n-----\n"
