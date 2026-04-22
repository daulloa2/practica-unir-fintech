"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending = True # Por defecto es ascendente

    # Cambiamos para aceptar 3 o 4 argumentos
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        
        # Si pasan el parámetro de orden (ej: "desc" o "asc")
        if len(sys.argv) == 4:
            ascending = sys.argv[3].lower() != "desc"
    else:
        print("Uso: python3 main.py <fichero> <eliminar_duplicados: yes/no> [orden: asc/desc]")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    # Le pasamos nuestra variable 'ascending' a la función de ordenamiento
    print(sort_list(word_list, ascending=ascending))