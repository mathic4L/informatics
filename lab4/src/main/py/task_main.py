from lex import tokenize

import os
# import sys

def my_read():
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'resources', 'from.yaml')
    return open(file_path, "r").read()

def my_write(output):
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'resources', 'to.yaml')
    return open(file_path, "w").write()

def main():
    string = my_read()
    tokens = tokenize(string)
    print(tokens)
    # if(my_write())


main()

