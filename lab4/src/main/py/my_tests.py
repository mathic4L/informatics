from lex import tokenize
from parse_obj import *
from pythonize_obj import pythonize_obj
from jsonize import jsonize
from my_io import *

def test_data_dir(file_name):
    return '..', '..', 'test', 'resources', file_name

def test_obj():
    string = my_read(test_data_dir('obj.yaml'))
    tokens = tokenize(string)
    tokens = tokens[1:]
    obj = parse_obj(tokens)[0]
    print(type(obj))

def test_arr():
    string = my_read(test_data_dir('arr.yaml'))
    tokens = tokenize(string)
    tokens = tokens[1:]
    arr_in_obj = parse_obj(tokens)[0]
    print(arr_in_obj)

def test_arr_2():
    string = my_read(test_data_dir('arr_2.yaml'))
    tokens = tokenize(string)
    tokens = tokens[1:]
    arr_in_obj = parse_obj(tokens)[0]
    print(arr_in_obj)

def test_obj_n_arr():
    string = my_read(test_data_dir('from.yaml'))
    tokens = tokenize(string)
    tokens = tokens[1:]
    arr_in_obj = parse_obj(tokens)[0]
    print(arr_in_obj)

def test_pythonize_obj():
    string = my_read(test_data_dir('obj.yaml'))
    tokens = tokenize(string)
    tokens = tokens[1:]     
    obj = parse_obj(tokens)[0]
    pythonized_obj = pythonize_obj(obj)
    print(pythonized_obj)

def test_pythonize_arr():
    string = my_read(test_data_dir('arr.yaml'))
    tokens = tokenize(string)
    tokens = tokens[1:]     
    obj = parse_obj(tokens)[0]
    pythonized_arr = pythonize_obj(obj)
    print(pythonized_arr)

def test_jsonize():
    string = my_read(test_data_dir('from.yaml'))
    tokens = tokenize(string)
    tokens = tokens[1:]     
    obj = parse_obj(tokens)[0]
    pythonized = pythonize_obj(obj)
    jsonized = jsonize(pythonized)
    print(pythonized)
    