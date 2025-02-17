def main():
    file_path = "books/frankenstein.txt"
    book = read_book(file_path)
    nb_words = count_words(book)
    nb_characters = count_characters(book)
    print(f"--- Begin report of {file_path} ---")
    print(f"{nb_words} words in the document")
    print("")
    report(nb_characters)
    print("--- End report ---")
    
def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_list = text.split()
    number_words = len(word_list)
    return number_words

def count_characters(text):
    dico = {}
    text = text.lower()
    list_characters = list(text)
    for character in list_characters:
        if character in dico:
            continue
        number_character = list_characters.count(character)
        dico[character] = number_character            
    return dico

def report(dico):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'y', 'z']
    for letter in alphabet:
        if letter in dico:
            value = dico[letter]
            print(f"The {letter!r} character was found {value} times")
    
main()