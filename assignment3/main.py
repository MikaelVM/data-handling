"""Solutions to assignment 3. - Theme: File handling and error management."""
from pathlib import Path
from helper_functions import FileHandler
import pandas as pd


if __name__ == "__main__":

    data_folder_path = Path("data")
    correct_file_path = data_folder_path / "source_data.csv"
    incorrect_file_path = data_folder_path / "non_existent_file.csv"
    # Manually set this file to be write-protected before running the code
    write_protected_file_path = data_folder_path / "write_protected.csv"

    # Part 1: Read an incorrect file path and handle the FileNotFoundError
    try:
        file_handler = FileHandler(incorrect_file_path)
        print(file_handler.read_file())

    except FileNotFoundError:
        print(f"File not found, incorrect path at {incorrect_file_path.absolute()}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Part 2: Read a file path and handle incorrect formatting of the file contents
    try:
        data_frame = pd.read_csv(correct_file_path, delimiter=',',
                                 dtype={"customer_id": "int",
                                        "name": "string",
                                        "email": "string",
                                        "purchase_amount": "int"})
    except Exception as e:
        print(f"An error occurred: {e}")

    # Part 3: Write to a write-protected file and handle the PermissionError
    try:
        file_handler = FileHandler(write_protected_file_path)
        file_handler.write_to_file("This is a test.")
    except PermissionError:
        print(f"Permission denied, cannot write to file at {write_protected_file_path.absolute()}.")
    except Exception as e:
        print(f"An error occurred: {e}")

