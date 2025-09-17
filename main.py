from stats import count_words
from stats import count_chars
from stats import sort_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_filepath = "books/frankenstein.txt"
    frankenstein_book = get_book_text(book_filepath)

    word_count = count_words(frankenstein_book)
    message = f"Found {word_count} total words"

    char_counts = count_chars(frankenstein_book)
    sorted_char_counts = sort_dict(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(message)
    print("--------- Character Count -------")
    for item in sorted_char_counts:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
        else:
            continue
    print("============= END ===============")


main()
