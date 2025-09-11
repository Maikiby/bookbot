def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_text):
    num_words = 0
    word_list = book_text.split()
    for word in word_list:
        num_words += 1
    return num_words

def main():
    word_count = count_words(get_book_text("./books/frankenstein.txt"))  
    message = f"{word_count} words found in the document"
    print(message)

main()
