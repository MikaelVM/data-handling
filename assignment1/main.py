"""Solutions to assignment 1 - Theme: Reintroduction to Python."""
from pathlib import Path
from statistics import median
from string import ascii_lowercase
from statistics import mean

import matplotlib.pyplot as plt
from helper_functions.file_reader import FileReader
from wordcloud import WordCloud

if __name__ == "__main__":

    print("Part 1.1 - Loading the file into a list of names")
    file_path = Path("./data/Navneliste.txt")
    file_reader = FileReader(file_path)
    names = file_reader.read_file_with_split(",")
    print(f"Proof: \n{names}\n")

    print("Part 1.2 - Sort the list alphabetically.")
    names.sort()
    print(f"Proof: \n{names}\n")

    print("Part 1.3 - Sort the list by length")
    names.sort(key=len)
    print(f"Proof: \n{names}\n")

    print("Part 1.4 - Create a dict that contain each character as key and values as how many times that name occurs"
          "in the list of names")
    letter_count = dict.fromkeys(ascii_lowercase, 0)

    for name in [x.lower() for x in names]:
        for character in name:
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1
    print(f"Proof: \n{letter_count}\n")

    print("Part 1e.1 - Visualise the frequency of every letter as a histogram and/or bar plot.")
    letter_count_bar = plt.bar(letter_count.keys(), letter_count.values())
    plt.title("Proof for Part 1e.1 (bar plot)")
    plt.show()

    print("Part 1e.2 - Create a word cloud from the content of the file.")
    names_str = file_reader.read_file()
    names_wordcloud = WordCloud().generate(names_str)
    plt.imshow(names_wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Proof for Part 1e.2 (word cloud)")
    plt.show()

    print("Part 1e.3 - Analyze length of names in the data set")
    names_len = []
    for name in names:
        names_len.append(len(name))

    names.sort()
    print(f"Proof: \nMedian: {median(names_len)}\nAverage: {mean(names_len)}\n")




