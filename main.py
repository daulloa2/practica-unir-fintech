"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

MESSAGES = {
    "missing_args": "You must provide the filename as the first argument",
    "second_arg": "The second argument indicates whether duplicates should be removed",
    "reading_file": "Reading words from file {}",
    "file_not_found": "File {} does not exist",
    "invalid_type": "Cannot sort object of type {}"
}

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(MESSAGES["invalid_type"].format(type(items)))

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES

    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        
        # Si pasan el parámetro de orden (ej: "desc" o "asc")
        if len(sys.argv) == 4:
            ascending = sys.argv[3].lower() != "desc"
    else:
        print(MESSAGES["missing_args"])
        print(MESSAGES["second_arg"])
        sys.exit(1)

    print(MESSAGES["reading_file"].format(filename))

    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(MESSAGES["file_not_found"].format(filename))
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    # Le pasamos nuestra variable 'ascending' a la función de ordenamiento
    print(sort_list(word_list, ascending=ascending))