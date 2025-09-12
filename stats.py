def count_words(book_text):
    num_words = 0
    word_list = book_text.split()
    for word in word_list:
        num_words += 1
    return num_words
