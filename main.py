from stats import count_words
from stats import count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    frankenstein_book = get_book_text("books/frankenstein.txt")
    word_count = count_words(frankenstein_book)  
    message = f"{word_count} words found in the document"
    print(message)
    char_counts = count_chars(frankenstein_book)
    print(char_counts)

main()
