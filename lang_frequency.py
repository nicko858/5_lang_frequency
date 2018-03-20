import sys
from collections import Counter


def load_data(filepath):
    with open(filepath, "r") as source_file:
        return source_file.read()


def get_most_frequent_words(text):
    words_count = 10
    word_freqs = Counter(text.split()).most_common(words_count)
    if word_freqs:
        return word_freqs
    else:
        return None


if __name__ == "__main__":
    script_usage = "lang_frequency.py  <path to file>"
    if len(sys.argv) != 2:
        print("Incorrect line argument!""\n""Using: {}".format(script_usage))
    else:
        load_file = load_data(sys.argv[1])
        word_list = get_most_frequent_words(load_file)
        if word_list:
            for word, count in word_list:
                print (word, count)
        else:
            exit("The source file is empty!")
