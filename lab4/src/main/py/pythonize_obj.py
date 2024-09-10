from util import *
from gramatics import *

def pythonize_obj(items):
    py_obj = {}
    lex_obj = items[1]

    for item in lex_obj:
        key, value = item
        if value[0] == Token_type.obj:
            py_obj[key[1]] = pythonize_obj(value)
        elif value[0] == Token_type.arr:
            py_obj[key[1]] = pythonize_arr(value)
        else:
            py_obj[key[1]] = pythonize_simple(value)

    return py_obj

def pythonize_arr(elements):
    arr = []
    lex_arr = elements[1]

    for el in lex_arr:
        if el[0] == Token_type.obj:
            arr.append(pythonize_obj(el))
        elif el[0] == Token_type.arr:
            arr.append(pythonize_arr(el))
        else:
            arr.append(pythonize_simple(el))

    return arr

def pythonize_simple(value):
    return value[1]





