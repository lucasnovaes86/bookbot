file_path = "/home/spikesama/workspace/github.com/lucas/bookbot/books/frankenstein.txt"

def main():
    content = get_book_text(file_path)
    words = get_num_words(content)
    print (f"Found {words} total words")

def get_book_text(p):
    with open(p) as f:
        return f.read()
    
from stats import get_num_words

main()