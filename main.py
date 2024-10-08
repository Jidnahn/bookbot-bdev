def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    words = word_count(text)
    letters = letter_count(text)
    report(path, words, letters)

def word_count(text):
    split_text = text.split()
    return len(split_text)

def get_text(path):
    with open(path) as f:
        return f.read()

def letter_count(text):
    letters = {}
    for c in text:
        lowered_letter = c.lower()
        if lowered_letter not in letters:
            letters[lowered_letter] = 0
        letters[lowered_letter] += 1
    return letters

def report(path, word_count, letter_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for letter in letter_count: 
        if not letter.isalpha():
            continue
        print(f"The '{letter}' character was found {letter_count[letter]} times")
    print("\n--- End report ---")


main()