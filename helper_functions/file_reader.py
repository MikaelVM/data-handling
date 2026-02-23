"""Module to read a file and return its contents in different formats."""
from pathlib import Path


class FileReader:
    """Class to read a file and return its contents."""

    def __init__(self, file_path: Path):
        """Initialize the FileReader with the given file path.

        Args:
            file_path (Path): The path to the file to be read.
        """
        self.file_path = file_path

    def set_file_path(self, file_path: Path) -> None:
        """Set the file path for the FileReader.

        Args:
            file_path (Path): The new path to the file to be read.
        """
        self.file_path = file_path

    def read_file(self) -> str:
        """Read the file and returns its contents as a string."""
        with open(self.file_path, 'r') as file:
            return file.read()

    def read_file_with_split(self, delimiter: str) -> list[str]:
        """Read the file and returns its contents as a list of strings, split by the given delimiter.

        Args:
            delimiter (str): The delimiter to split the file contents by.
        """
        with open(self.file_path, 'r') as file:
            return file.read().split(delimiter)
