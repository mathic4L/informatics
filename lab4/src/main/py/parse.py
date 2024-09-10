from parse_arr import parse_arr
from parse_obj import parse_obj

def parse_simple_value(tokens):
    return tokens[1][1], tokens[1:]

def parse(tokens):
    funcs = [parse_obj, parse_arr, parse_simple_value]
    for func in funcs:
        value, tokens = func(tokens)
        if value is not None:
            return value, tokens

    raise Exception("Incorrect syntax")


# def parse(tokens):
#     tokens_fst = tokens[0]
#     tokens_scd = tokens[1]
#     if tokens_fst[0] == Token_type.obj_or_arr_start:
#         if tokens_scd[]:
#             return parse_obj(tokens)
#         elif '''''':
#             return parse_arr(tokens)
#         else:
#             raise Exception("Incorrect syntax")
#     else:
#         return tokens_fst[1], tokens[1:]


# def loads(string):
#     return parse_obj(tokenize(string)[1:])[0]
