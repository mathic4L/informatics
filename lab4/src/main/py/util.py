from gramatics import *
exception_prefix = "exception: "

def arr_startswith(arr, prefix):
    return arr[:len(prefix)] == prefix

def arr_lstrip(arr, tobe_striped):
    tobo_striped_len = len(tobe_striped)
    return arr[tobo_striped_len:] if arr[:tobo_striped_len] == tobo_striped_len else arr

def get_indent_cnt(tokens):
    uint_indent_cnt = 0
    qualifiers_cnt = 0
    while (True):
        if tokens[0][0] == Token_type.unit_indent:
            uint_indent_cnt += 1
            tokens = tokens[1:]
        elif tokens[0][0] == Token_type.array_member_qualifier:
            qualifiers_cnt += 1
            tokens = tokens[1:]
        else:
            break

    return uint_indent_cnt, qualifiers_cnt

def cut_indents(tokens, times):
    for i in range(0, times):
        tokens = tokens[1:]
    
    return tokens  

def cnt_indents(tokens):
    cnt = 0