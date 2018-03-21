import sys
from collections import Counter
import re


def load_data(filepath):
    with open(filepath, "r") as source_file:
        return source_file.read()


def get_most_frequent_words(text):
    words_count = 10
    get_words = re.findall('\w+', text.lower())
    return Counter(get_words).most_common(words_count)


if __name__ == "__main__":
    script_usage = "lang_frequency.py  <path to file>"
    if len(sys.argv) != 2:
        exit("Incorrect line argument!""\n""Using: {}".format(script_usage))
    load_file = load_data(sys.argv[1])
    ten_freq_words = get_most_frequent_words(load_file)
    for word, count in ten_freq_words:
        print(word, count)
