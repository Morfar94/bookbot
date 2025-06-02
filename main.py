from stats import get_book_text
from stats import count_words
from stats import count_letters
from stats import sort_on
from stats import reformat_dict

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_amount = count_words(book_text)
    letter_amount = count_letters(book_text)
    list_of_chars = reformat_dict(letter_amount)
    print(f'{word_amount} words found in the document')
    print(list_of_chars)

main()