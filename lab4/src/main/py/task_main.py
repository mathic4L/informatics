from lex import tokenize
from parse_obj import *
from pythonize_obj import pythonize_obj
from my_tests import *
from my_io import *

def main():

    # test_obj()
    # test_pythonize_obj()

    # test_arr()
    # test_arr_2()
    # test_pythonize_arr()
    
    # test_obj_n_arr()
    # test_jsonize()

    yaml_str = my_read(('..', 'resources', 'from.yaml'))
    tokens = tokenize(yaml_str)
    tokenized_obj = parse_obj(tokens[1:])[0]
    python_obj = pythonize_obj(tokenized_obj)
    json_str = jsonize(python_obj)
    my_write(('..', 'resources', 'to_main.json'), json_str)


main()



