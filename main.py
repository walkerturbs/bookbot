def main(): 
    path_to_book = "books/frankenstein.txt"
    book_text = get_text_from_book(path_to_book)
    word_count = count_words(book_text)
    char_dict = count_charchters(book_text)
    char_count = char_dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count:,} words found in the document")
    print(" ")
    for char in char_count:
        if char["char"].isalpha():
            print(f"The '{char['char']}' character was found {char['num']:,} times")
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_charchters(text):
    lowercase_text = text.lower()
    charchter_dict = {}
    
    for ch in lowercase_text:
        if ch not in charchter_dict:
            charchter_dict[ch] = 1
        else:
            charchter_dict[ch] += 1
    
    return charchter_dict

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_text_from_book(path):
    with open(path) as f:
        return f.read()

main()