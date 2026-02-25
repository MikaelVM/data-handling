from helper_functions import FileHandler
from pathlib import Path
from enum import Enum
from datetime import datetime

class LogLevel(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class Logger:
    def __init__(self, log_folder_path: Path):
        self.log_folder_path = log_folder_path

    def log(self, message: str, level: LogLevel) -> None:
        log_file_path = self.log_folder_path / self._log_file_name(level)
        file_handler = FileHandler(log_file_path)
        message = file_handler.read_file() + self._log_message(message) if log_file_path.exists() \
            else self._log_message(message)

        file_handler.write_to_file(message)

    def clear_logs(self) -> None:
        for level in LogLevel:
            log_file_path = self.log_folder_path / self._log_file_name(level)
            log_file_path.unlink()

    @staticmethod
    def _log_file_name(level: LogLevel) -> str:
        return f"log_{level.value}.txt"

    @staticmethod
    def _log_message(message: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
        return f"{timestamp}: \n{message}\n-----\n"
