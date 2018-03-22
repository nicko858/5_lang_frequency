# Frequency Analysis of Words

Script takes the input path to a text file and output to the console 10 most popular words in this file in descending order of frequency.

# Quickstart

The program is represented by the module ```lang_frequency.py```.
Module ```lang_frequency.py``` contains the following functions:

- ```load_data()``` - accepts the input to a file with arbitrary data in text format and reads the file content
- ```get_most_frequent_words()``` - accepts the file content  from the previous function and the words count(entering by user as a script-parametr ) Finally function returns most popular words in this file in descending order of frequency.

The program uses these libs from Python Standart Library:

```python
from collections import Counter
import re
import argparse

```

How in works:
- Using argparse, the program reads  the first command-line argument(path to text-file) and the second argument (words count need to display)
- loads it using  ```load_data())``` -function
- With ```get_most_frequent_words()``` -function, return most popular words in this file in descending order of frequency. 

Example of script launch on Linux, Python 3.5:

```bash

$ python lang_frequency.py <path to file> <words_count>

```
in the console  output you will see something  like this:
```bash
в 4
и 4
на 3
такой 2
можно 2
с 2
должен 2
частые 1
написать 1
ему 1
```

The program check command-line arguments and if it is wrong,  you will see the warning message:
```usage: lang_frequency.py [-h] source_text words_count```
```lang_frequency.py: error: the following arguments are required: words_count.```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

