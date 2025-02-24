def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text_from_book):
    words = text_from_book.split()
    word_count = len(words)
    return word_count

def get_num_characters(text_from_book):
    char_counts = {}
    lwords = text_from_book.lower()
    for char in lwords:
        if char in char_counts: 
            char_counts[char] += 1
        else:
            char_counts[char] = 1 
    return char_counts

def convert_dict_to_list(dict): 
    list_of_dicts = [{"char": k, "num": v} for k, v in dict.items()]

    return list_of_dicts

def sort_on(dict):
    return dict["num"]