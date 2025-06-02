def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    word_amount = len(book_text.split())
    return word_amount

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_amount = count_words(book_text)
    print(f'{word_amount} words found in the document')

main()