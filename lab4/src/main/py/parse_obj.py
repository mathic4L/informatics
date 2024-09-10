from gramatics import *
from parse import parse

def parse_obj_body(tokens):
    obj = {}
    
    while True:
        key = tokens[0][1]
        tokens = tokens[1:]

        if type(key) is not str:
            raise Exception("Expected key of type string")

        if tokens[0] in KEY_DIVS:
            tokens = tokens[1:]
        else:
            raise Exception("Expected key terminator")

        value, tokens = parse(tokens)
        obj[key] = value

        if tokens[0][0] == Token_type.obj_or_arr_end:
            return obj, tokens[1:]
        elif tokens[0][0] == Token_type.line_break:
            continue
        else:
            raise Exception("Expected linebreak or endof_arr_or_obj")

def parse_obj(tokens):
    
    if tokens[0][0] != Token_type.obj_or_arr_start and tokens[0][0] != Token_type.string:
        return None, tokens

    tokens = tokens[1:]
    if tokens[0][0] == Token_type.obj_or_arr_end:
        return {}, tokens[1:]
    
    return parse_obj_body(tokens)