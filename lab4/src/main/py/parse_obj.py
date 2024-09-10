from gramatics import *
from util import *


def parse_obj(tokens):
    entries = []
    key = None
    value = None

    uint_indent_start, qualifiers_start = get_indent_cnt(tokens)
    indents_start = uint_indent_start + qualifiers_start
    qualifiers_sum = 0

    while True:
        if tokens[0][0] == Token_type.end_of_file: # tokens end
            return (Token_type.obj, entries), tokens
        uint_indent_curr, qualifiers_curr = get_indent_cnt(tokens)
        indents_curr = uint_indent_curr + qualifiers_curr
        qualifiers_sum += qualifiers_curr
        if qualifiers_sum == 2: # obj end in arr
            return (Token_type.obj, entries), tokens
        elif indents_curr < uint_indent_start: # end of obj
            break

        tokens = cut_indents(tokens, indents_start)

        key = tokens[0]
        if key[0] == Token_type.string:
            tokens = tokens[1:]
            if tokens[0][0] == Token_type.colon_space:  # scalar
                value, tokens = parse_simple(tokens[1:])
            elif tokens[0][0] == Token_type.colon_linebreak:  # obj or arr
                tokens = tokens[1:]
                if (
                    tokens[indents_start + 1][0] == Token_type.array_member_qualifier
                ):  # arr
                    value, tokens = parse_arr(tokens)
                else:  # obj
                    # tokens = cut_indents(tokens, start_indent + 1)
                    value, tokens = parse_obj(tokens)
            else:
                raise Exception(f"{exception_prefix}incorrect syntax in objects value")
        else:
            raise Exception(f"{exception_prefix}key should be string")

        entries.append((key, value))
        if tokens[0][0] == Token_type.line_break:
            tokens = tokens[1:]  # cut \n

    return (Token_type.obj, entries), tokens


def parse_arr(tokens):
    arr_members = []
    value = None

    uint_indent_start, qualifiers_start = get_indent_cnt(tokens)
    indents_start = uint_indent_start + qualifiers_start

    while True:
        uint_indent_curr, qualifiers_curr = get_indent_cnt(tokens)
        indents_curr = uint_indent_curr + qualifiers_curr
        if tokens[0][0] == Token_type.end_of_file:
            return (Token_type.arr, arr_members), tokens
        elif indents_curr < indents_start:
            break

        if tokens[indents_start + 1][0] == Token_type.line_break:
            value, tokens = parse_simple(tokens[indents_start:])
            if tokens[0][0] == Token_type.line_break:
                tokens = tokens[1:]  #
        elif tokens[indents_start + 1][0] == Token_type.colon_space:
            value, tokens = parse_obj(tokens)
        elif tokens[indents_start + 0][0] == Token_type.array_member_qualifier:
            value, tokens = parse_arr(tokens)
        else:
            raise Exception(f"{exception_prefix}incorrect syntax in array")

        # tokens = cut_indents(tokens, start_indent) # indents + '- '
        # tokens = tokens[1:]  # skip "- "
        arr_members.append(value)

    return (Token_type.arr, arr_members), tokens


def parse_simple(tokens):
    return tokens[0], tokens[1:]


def parse_simple_arr(tokens):
    return tokens[0], tokens[1:]
