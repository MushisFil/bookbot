import string


def read_frankenstein():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
    return len(words)

def count_letters():
    letter_dict = dict()
    alphabets = set(string.ascii_lowercase)
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
        for char in lowered_string:
            if char in letter_dict.keys():
                letter_dict[char] += 1
            elif char in alphabets:
                letter_dict[char] = 1
    return letter_dict


def sort_on(dict):
    return dict["num"]


if __name__=="__main__":
    print("--- Herein lies the fabled report of books/frankenstein.txt ---")
    print(f'{count_words()} words found in the document\n') 

    letter_dict = count_letters()
    # Create a list of dicts
    letter_dictList = []
    for key in letter_dict.keys():
        letter_dictList.append({"character": key, "num":letter_dict[key]})
    letter_dictList.sort(reverse=True, key=sort_on)

    for letterDict in letter_dictList:
        print(f"The '{letterDict["character"]}' character was found {letterDict["num"]} times")
    print('--- End report ---')