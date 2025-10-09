import sys

# Importa funcoes do arquivo stats.py
from stats import (
        get_num_words,
        get_num_char,
        get_sorted_char
        )


def main():
    if len(sys.argv) < 2:
        print ("Usage Error: Please provide a file path as an argument.")
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    text = get_book_text(file_path)
    num_words = get_num_words(text)
    counted_characters = get_num_char(text)
    sorted_characters = get_sorted_char(counted_characters)
    print_result(file_path, num_words, sorted_characters)

# Recebe o caminho do arquivo e abre ele como texto
def get_book_text(p):
    with open(p) as f:
        return f.read()

def print_result(file_path, num_words, sorted_characters):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {file_path}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for c in sorted_characters:
        if not c["char"].isalpha():
            continue
        print(f"{c["char"]}: {c["count"]}")

    print ("============= END ===============")



main()
