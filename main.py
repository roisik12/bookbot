def main():
        path = 'books/frankenstein.txt'
        text = book_text(path)
        count = words_count(text)
        dict = characters_count(text)
        
        list = dict_to_list(dict)
        list.sort(reverse=True,key=sort_on)
        print(f"--- Begin report of {path} ---")
        print(f"{count} words were found in the text\n")
        for set in list:
            if(set.get('character').isalpha()): # check if a string only contains characters from the alphabet
                print(f"The '{set.get('character')}' character was found {set.get('count')} times")
        print(f"--- End report ---")

#creates the list of dictionaries with 'character' and 'count' keys
def dict_to_list(dict):
     list = []
     for char in dict:
          list.append({"character":char,"count":dict.get(char)})
     return list

def sort_on(dict):
     return dict["count"]
# returns the dictionary with the count of the characters in the text
def characters_count(text):
    words = text.split()
    characters_dict = {}
    for word in words:
        for character in word:
            lowered_character = character.lower()
            characters_dict.setdefault(lowered_character,0)
            characters_dict[lowered_character]=(characters_dict.get(lowered_character)+1)
    return characters_dict
# returns count of words in the text
def words_count(text):
     words = text.split()
     return len(words)
# returns the text
def book_text(path):
    with open(path) as f:
        return f.read()
main()