def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    print(f"--- Begin report of {path} ---")
    print(f"Number of words: {word_counted(text)}")
    
    # Get the character counts
    char_counts = character_counted(text)
    
    # Sort the character counts
    sorted_chars = sort_on(char_counts)
    
    # Print each character and its count
    for item in sorted_chars:
        print(f"The '{item['character']}' character was found {item['num']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_counted(text):
    words = text.split()
    
    return len(words)

def character_counted(text):
    lowered_string = text.lower()
    characters = list(lowered_string)

    char_dictionary = {}
    for character in characters:
        if character.isalpha() == True:
            if character in char_dictionary:
                char_dictionary[character] += 1
            else:
                char_dictionary[character] = 1
    return char_dictionary

def sort_on(char_dictionary):
    list_of_dict_char = [{"character": key, "num": value} for key, value in char_dictionary.items()]    
    
    list_of_dict_char.sort(reverse=True, key=lambda item: item["num"])
    
    return list_of_dict_char

 
    


main()