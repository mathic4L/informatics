
from gramatics import *
from parse import parse

def parse_arr_body(tokens):
    arr = []
    
    while tokens[0][0] != Token_type.obj_or_arr_end:
        tokens = tokens[1:] # скипаем "-"
        value, tokens = parse(tokens)
        

def parse_arr(tokens):
    
    if tokens[0][0] == Token_type.arr_start and tokens[1][0] == Token_type.arr_end:
        return {}, tokens[2:]
    elif tokens[0][0] != Token_type.obj_or_arr_start or tokens[1][0] != Token_type.array_member_qualifier:
        return None, tokens 
    else:
        return parse_arr_body(tokens[1:])