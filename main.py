path = "/home/spikesama/workspace/github.com/lucas/bookbot/books/frankenstein.txt"

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    content = get_book_text(path)
    print (content)

main()