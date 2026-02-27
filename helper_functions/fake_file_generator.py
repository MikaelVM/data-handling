from faker import Faker
from faker.providers import BaseProvider
import csv
import random
from datetime import datetime

class FakeFileGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.faker = Faker()

    def set_file_path(self, file_path):
        self.file_path = file_path

    def generate_fake_movie_file(self, num_lines=100):
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
        """

        with open(self.file_path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Genre", "Premiere", "Runtime", "IMDB Score", "Language"])
            for _ in range(num_lines):
                writer.writerow(self._generate_fake_movie_data())

    def _generate_fake_movie_data(self):
        """Generates a single line of fake movie data."""

        title = self.faker.sentence(nb_words=3)
        genre = random.choice(['Documentary', 'Thriller', 'Mystery', 'Horror', 'Action', 'Comedy', 'Drama', 'Romance'])
        premiere = datetime.strftime(self.faker.date_time_this_decade(), "%B %d, %Y")
        runtime = random.randint(60, 220)
        imdb_score = round(random.uniform(1.0, 10.0), 1)
        language = self.faker.language_name()

        return [title, genre, premiere, runtime, imdb_score, language]
