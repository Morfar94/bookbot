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
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {word_amount} total words')
    print('--------- Character Count -------')

    list_of_chars.sort(reverse=True,key=sort_on)
    
    for item in list_of_chars:
        amount = item['num']
        character = item['char']
        if character.isalpha():
            print(f'{character}: {amount}')

main()