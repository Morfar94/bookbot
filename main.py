from stats import get_book_text
from stats import count_words
from stats import count_letters

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_amount = count_words(book_text)
    letter_amount = count_letters(book_text)
    print(f'{word_amount} words found in the document')
    print(letter_amount)

main()