"""Solutions to bonus assignments - Theme: Reading and processing large data files using generators."""

from pathlib import Path
from typing import Generator

from helper_functions import FakeFileGenerator

if __name__ == "__main__":
    # Create an instance of the FakeFileGenerator class
    generator = FakeFileGenerator(Path('./data'))

    file_name = 'fake_movie_data'

    print("Part 1: Data Generation using Faker library")
    print("Checking if data file exists...")
    if not (Path(f'./data/{file_name}.csv').exists()):
        print("Data file does not exist. Generating new file...")
        generator.generate_fake_movie_file(num_lines=10000, file_name=file_name, append_to_file=False)
    else:
        print("Data file already exists, skipping file generation.")

    print("Part 2: Reading and processing the large data file:")

    def file_generator(file_path: str) -> Generator[str, None, None]:
        """Read a file line by line from a file and yields each line.

        Args:
            file_path (str): The path to the file to be read.

        Yields:
            str: The next line in the file.
        """
        with open(file_path, 'r') as file:
            for line in file:
                yield line

    data_generator = file_generator(f'./data/{file_name}.csv')

    print("First 10 lines of the file:")
    for _ in range(10):
        print(next(data_generator).strip())
