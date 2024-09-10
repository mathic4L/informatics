from lex_regexp import tokenize
from parse_obj import *
from pythonize_obj import pythonize_obj
from my_tests import *
from my_io import *

def main():

    yaml_str = my_read(('..', 'resources', 'from.yaml'))
    tokens = tokenize(yaml_str)
    tokenized_obj = parse_obj(tokens[1:])[0]
    python_obj = pythonize_obj(tokenized_obj)
    json_str = jsonize(python_obj)
    my_write(('..', 'resources', 'to_dop3.json'), json_str)


main()



