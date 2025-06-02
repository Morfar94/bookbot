def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    word_amount = len(book_text.split())
    return word_amount

def count_letters(book_text):
    lower_text = book_text.lower()
    letters_dictionary = {}
    for letter in lower_text:
        if letter in letters_dictionary:
            letters_dictionary[letter] = letters_dictionary[letter] + 1
        else:
            letters_dictionary[letter] = 1
    return letters_dictionary