import sys
from stats import get_book_text
from stats import get_num_words
from stats import get_num_characters
from stats import sort_on
from stats import convert_dict_to_list



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1] 
    words = get_book_text(path)
    word_count = get_num_words(words)
    character_count = get_num_characters(words)
   # print(f"These are the character counts: {character_count}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    dict_list = convert_dict_to_list(character_count)
    dict_list.sort(reverse=True, key=sort_on)
    for dict in dict_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
 

main()