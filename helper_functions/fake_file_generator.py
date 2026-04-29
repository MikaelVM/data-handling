"""Module for generating fake movie data files in the CSV format."""

import csv
import random
from datetime import datetime
from pathlib import Path

from faker import Faker
from faker.typing import SeedType
from rich.progress import track


class FakeFileGenerator:
    """Class for generating fake movie data files in the CSV format.

    Attributes:
        dir_path (Path): The directory path where the generated file will be saved.
        fake (Faker): An instance of the Faker class from the Faker library, used to generate fake data.
    """

    def __init__(self, dir_path: Path, faker_seed: SeedType = None) -> None:
        """Initialize the FakeFileGenerator instance.

        Args:
            dir_path (Path): The directory path where the generated file will be saved.
            faker_seed (int, optional): An optional seed value for the Faker instance to ensure reproducibility of the
             generated data. Defaults to None.
        """
        self.dir_path = dir_path
        self.fake = Faker()
        if faker_seed is not None:
            self.fake.seed_instance(faker_seed)

    def set_file_path(self, file_path: Path) -> None:
        """Set the directory path for the FakeFileGenerator instance.

        Args:
            file_path (Path): The new directory path where the generated file will be saved.
        """
        self.dir_path = file_path

    def generate_fake_movie_file(
            self,
            *,
            num_lines: int = 100,
            file_name: str = 'fake_movie_data',
            append_to_file: bool = False
    ) -> None:
        """Generate a csv file that simulates a series of movies.

        The file will contain the following columns:
        - Title: The title of the movie
        - Genre: The genre of the movie
        - Premiere: The premiere date of the movie
        - Runtime: The runtime of the movie in minutes
        - IMDB Score: The IMDB score of the movie
        - Language: The language of the movie

        Args:
            num_lines (int): The number of lines to generate in the file (default: 100)
            file_name (str): The name of the file to be generated (default: 'fake_movie_data').
                File extension will be added automatically as '.csv'.
            append_to_file (bool): Whether to append to the file if it already exists (default: False).
                If False, the file will be overwritten if it already exists.
        """
        file_name = file_name + '.csv'

        if append_to_file and (self.dir_path / file_name).exists():
            mode = 'a'
            print(f"{datetime.now()}: Appending {num_lines:,} lines to existing file '{file_name}'.")
        else:
            mode = 'w'
            print(f"{datetime.now()}: Creating new file '{file_name}' with {num_lines:,} lines.")

        with open(self.dir_path / file_name, mode, newline='') as csvfile:
            writer = csv.writer(csvfile)

            if mode == 'w':
                writer.writerow(['Title', 'Genre', 'Premiere', 'Runtime', 'IMDB Score', 'Language'])

            for _ in track(range(num_lines), description="Working..."):
                writer.writerow(self._generate_fake_movie_data())

        print(f"{datetime.now()}: File generation complete.")

    def _generate_fake_movie_data(self) -> list:
        """Generate a single line of fake movie data."""
        title = self.fake.sentence(nb_words=3)
        genre = random.choice(['Documentary', 'Thriller', 'Mystery', 'Horror', 'Action', 'Comedy', 'Drama', 'Romance'])
        premiere = datetime.strftime(self.fake.date_time_this_decade(), '%B %d, %Y')
        runtime = random.randint(50, 220)
        imdb_score = round(random.uniform(1.0, 10.0), 1)
        language = self.fake.language_name()

        return [title, genre, premiere, runtime, imdb_score, language]
