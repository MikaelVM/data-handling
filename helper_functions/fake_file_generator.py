from faker import Faker
from faker.providers import BaseProvider
import csv
import random
from datetime import datetime
from  pathlib import Path
from rich.progress import track

class FakeFileGenerator:
    def __init__(self, dir_path: Path, faker_seed=None):
        self.dir_path = dir_path
        self.fake = Faker()
        if faker_seed is not None:
            self.fake.seed_instance(faker_seed)


    def set_file_path(self, file_path: Path) -> None:
        self.dir_path = file_path

    def generate_fake_movie_file(
            self,
            *,
            num_lines=100,
            file_name: str = 'fake_movie_data',
            append_to_file: bool = False
    ) -> None:
        """Generates a csv file that simulates a series of movies.

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

            for _ in track(range(num_lines), description= "Working..."):
                writer.writerow(self._generate_fake_movie_data())

        print(f"{datetime.now()}: File generation complete.")

    def _generate_fake_movie_data(self) -> list:
        """Generates a single line of fake movie data."""

        title = self.fake.sentence(nb_words=3)
        genre = random.choice(['Documentary', 'Thriller', 'Mystery', 'Horror', 'Action', 'Comedy', 'Drama', 'Romance'])
        premiere = datetime.strftime(self.fake.date_time_this_decade(), '%B %d, %Y')
        runtime = random.randint(50, 220)
        imdb_score = round(random.uniform(1.0, 10.0), 1)
        language = self.fake.language_name()

        return [title, genre, premiere, runtime, imdb_score, language]
