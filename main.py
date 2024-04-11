def main ():
    book = get_book()
    number_words = get_words(book)
    letter_count = get_letters(book)
    sorted_letters = sort_letters(letter_count)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{number_words} words found in the document")
    print()

    for i in sorted_letters:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")

def get_book():
    with open("/home/rschnitzel/workspace/github.com/rschnitzel/bookbot/books/frankenstein.txt") as book:
        return book.read()
    
def get_words(b):
    words = b.split()
    return len(words)

def get_letters(b):
    lower_case = b.lower()
    letter_count = {}
    for l in lower_case:
        if l in letter_count:
            letter_count[l] += 1
        else:
            letter_count[l] = 1

    return letter_count

def sort_on(d):
    return d["num"]

def sort_letters(l):
    sorted_letters = []
    for ch in l:
        sorted_letters.append({"char": ch, "num": l[ch]})
    sorted_letters.sort(reverse=True, key=sort_on)

    return sorted_letters


main()