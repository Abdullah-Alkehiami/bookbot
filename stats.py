def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(words):
    character_count_dic = {}
    for letter in words:
        if letter.lower() in character_count_dic:
            character_count_dic[letter.lower()] += 1
        else:                
            character_count_dic[letter.lower()] = 1
    return character_count_dic

def sort_on(items):
    return items["count"]

def convert_to_list(char_dictionary):
    char_list_of_dic = []
    for key, value in char_dictionary.items():
        char_list_of_dic.append({"char": key, "count": value})
    char_list_of_dic.sort(reverse=True, key=sort_on)
    return char_list_of_dic
