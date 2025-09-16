def count_words(book_text):
    num_words = 0
    word_list = book_text.split()
    for word in word_list:
        num_words += 1
    return num_words

def count_chars(book_text):
    char_dict = {}
    for char in book_text:
        lowered_char = char.lower()
        if lowered_char in char_dict:
            char_dict[lowered_char] += 1
        else:
            char_dict[lowered_char] = 1

    return char_dict
