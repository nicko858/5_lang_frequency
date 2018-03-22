import sys
from collections import Counter
import re


def load_data(filepath):
    with open(filepath, "r") as source_file:
        return source_file.read()


def get_most_frequent_words(text, words_count):
    only_words = re.findall('\w+', text.lower())
    return Counter(only_words).most_common(words_count)


if __name__ == "__main__":
    script_usage = "lang_frequency.py <path to file> <words_count>"
    if len(sys.argv) != 3:
        exit("Incorrect line argument!\nUsing: {}".format(script_usage))
    file_to_load = load_data(sys.argv[1])
    freq_words = get_most_frequent_words(file_to_load, int(sys.argv[2]))
    for word, count in freq_words:
        print(word, count)