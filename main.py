from stats import get_book_text

from stats import count_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_amount = count_words(book_text)
    print(f'{word_amount} words found in the document')

main()