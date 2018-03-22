from collections import Counter
import re
import argparse


def load_data(filepath):
    with open(filepath, "r") as source_file:
        return source_file.read()


def get_most_frequent_words(text, words_count):
    only_words = re.findall("\w+", text.lower())
    return Counter(only_words).most_common(words_count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="How to run lang_frequency.py:")
    parser.add_argument("source_text",
                        help="Specify the path to the source text file")
    parser.add_argument("words_count", type=int,
                        help="Specify the words count need to display")
    args = parser.parse_args()
    script_usage = "lang_frequency.py <path to file> <words_count>"
    try:
        loaded_text = load_data(args.source_text)
    except IOError:
        exit("No such file or directory {}".format(args.source_text))
    most_freq_words = get_most_frequent_words(loaded_text, args.words_count)
    for word, count in most_freq_words:
        print(word, count)
