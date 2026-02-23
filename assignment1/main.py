from pathlib import Path
from helper_functions.file_reader import FileReader
from string import ascii_lowercase
import collections

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
    letter_count = {}

    for name in [x.lower() for x in names]:
        for character in name:
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1
    print(f"Proof: \n{letter_count}\n")

