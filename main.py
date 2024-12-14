def main():
    book_path = 'books/frankenstein.txt'
    text = load_text(book_path)
    count = count_words(text)
    character_dict = count_characters(text)
    output_report(book_path, count, character_dict)

def load_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_count = {}
    for character in text:
        character = character.lower()
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def output_report(book, word_count, character_dict):
    print(f'--- Report of {book} ---\n')
    print(f'The number of words in the book is {word_count}.')
    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in alphabet:
        print(f"There are {character_dict[letter]} {letter}'s in the text.")

    print(f'\n--- End of Report ---')

if __name__ == "__main__":
    main()