from stats import count_words
from stats import get_book_text
from stats import count_characters
from stats import convert_to_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_dictionary = count_characters(text)
    list_of_characters = convert_to_list(character_dictionary)
    #print(text)
    # print(f"{word_count} words found in the document")
    # print(character_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in list_of_characters:
        print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")
    
main()