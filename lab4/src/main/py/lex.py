from gramatics import *


def lex_string(string):
    parsed = ""
    quotes = False

    if string[0] == DOUBLE_QUOTES:
        string = string[1:]
        quotes = True

    terminators_when_no_quotes = [COLON, LINE_BREAK]
    terminators_when_quotes = [DOUBLE_QUOTES]

    for c in string:
        to_break = False
        terminators = terminators_when_quotes if quotes else terminators_when_no_quotes
        for terminator in terminators:
            if c == terminator:
                to_break = True
                break
        if to_break:
            break
        else:
            parsed += c

    extra_shift = 1 if quotes else 0
    rest = string[len(parsed) + extra_shift :]
    return (Token_type.string.name, parsed, rest)


def lex_number(string):
    DIGITS = [str(d) for d in range(0, 10)]
    NUMBER_COMPONENTS = DIGITS + ["-", "."]

    token = None
    parsed = ""
    out = None

    for c in string:
        if c in NUMBER_COMPONENTS:
            parsed += c
        else:
            break

    len_parsed = len(parsed)
    string = string[len_parsed:]

    if len_parsed == 0:
        out = None
    elif string[0] != "\n":
        type, value, string = lex_string(string)
        return (type, parsed + value, string)
    elif "." in parsed:
        out = float(parsed)
    else:
        out = int(parsed)

    return (token, out, string)


def lex_values(string, map, token_type):

    token = None
    out = None

    for key, value in map.items():
        if string.startswith(key):
            token = token_type
            out = value
            string = string[len(key) :]

            break

    return (token, out, string)


def lex_bool(string):
    return lex_values(string, {"true": True, "false": False}, Token_type.null)


def lex_null(string):
    return lex_values(string, {"null": None}, Token_type.null)


def lex_array_member_qualifier(string):
    return lex_values(string, {"- ": None}, Token_type.array_member_qualifier)


def lex_doc_start(string):
    return lex_values(string, {DOC_START: DOC_START}, Token_type.doc_start)


def lex_borders(string, prev_indent):
    token = None
    out = None
    curr_indent = 0

    if string.startswith(KEY_VALUE_DIV_SCALAR):
        token = Token_type.simple_start
        string = string[2:]

    elif string.startswith(KEY_VALUE_DIV_ARR_OR_OBJ):
        token = Token_type.obj_or_arr_start
        string = string[2:]
        string = string.lstrip()

    elif string.startswith("\n"):
        string = string[1:]
        curr_indent, string = get_indent(string)
        out = get_borders(prev_indent - curr_indent)
        if out == []:
            token = Token_type.simple_end
            string = string.lstrip()
        else:
            token = Token_type.obj_or_arr_end

    return token, out, curr_indent, string


'''

передаем строку начиная с переноса строки
доходим до переноса строки
считаем отступы

'''

def lex_borders(string, prev_indent):
    token = None
    out = None
    curr_indent = 0

    if string.startswith("\n"):
        string = string[1:]
        curr_indent, string = get_indent(string)
        out = get_borders(prev_indent - curr_indent)
        if out == []:
            token = Token_type.simple_end
            string = string.lstrip()
        else:
            token = Token_type.obj_or_arr_end

    # elif string.startswith(KEY_VALUE_DIV_ARR_OR_OBJ):
    #     token = Token_type.obj_or_arr_start
    #     string = string[2:]
    #     string = string.lstrip()
    # return token, out, string

    return token, out, curr_indent, string

def lex_inline_border(string):
    return lex_values(string, {KEY_VALUE_DIV_SCALAR: KEY_VALUE_DIV_SCALAR}, Token_type.simple_start)


def get_indent(string):
    counter = 0
    while string[0:2] == SINGLE_INDENT:
        counter += 1
        string = string[2:]

    return counter, string


def get_borders_count(indent_delta):
    out = []
    token = (   
        (Token_type.obj_or_arr_start)
        if indent_delta > 0
        else (Token_type.obj_or_arr_end)
    )
    indent_delta = abs(indent_delta)
    while indent_delta > 0:
        out.append(token)

    return out


def tokenize(string):
    tokens = []

    type, value, string = lex_doc_start(string)
    if type != Token_type.doc_start:
        raise Exception("document start expected")

    prev_indent = 0
    # prev_indent = 0
    while len(string) > 0:
        value = None

        token, out, prev_indent, string = lex_borders(string, prev_indent)
        if token != None:
            if token != Token_type.obj_or_arr_end:
                tokens.append(
                    token,
                )
                continue
            else:
                tokens.extend(out)
                continue

        funcs = [
            lex_inline_border,
            lex_array_member_qualifier,
            lex_null,
            lex_number,
            lex_bool,
            lex_string,
        ]
        for func in funcs:
            type, value, string = func(string)
            if type is not None:
                tokens.append((type, value))
                break

        if type is not None:
            print("done")
            continue
        else:
            raise Exception("Unknown character")

    return tokens
