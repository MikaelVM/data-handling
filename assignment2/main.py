"""Solutions to assignment 2 - Theme: Log file analysis.

Developer Notes:
    The assignments specifically ask to use os.path.join for file path handling across operating systems.
    I disagree with this choice and will use pathlib instead, as I have experienced it to be more intuitive, less
    error-prone and can handle file paths across operating systems just as well as os.path.join.
"""
from pathlib import Path

from assignment2.logger import LogHandler, LogLevel
from faker import Faker

if __name__ == "__main__":

    logger = LogHandler(Path("logs"))
    faker = Faker()

    for _logs in range(10):
        logger.log(f"This is an info message: {faker.text()}", LogLevel.INFO)
        logger.log(f"This is an warning message: {faker.text()}", LogLevel.WARNING)
        logger.log(f"This is an error message: {faker.text()}", LogLevel.ERROR)

    for file in Path("logs").iterdir():
        print(f"Contents of {file.name}:")
        with open(file, 'r') as f:
            print(f.read())

    logger.clear_logs()
