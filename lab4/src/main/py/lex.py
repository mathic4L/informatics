from gramatics import *


def lex_string(string):
    parsed = ""
    quotes = False
    terminators = [COLON, LINE_BREAK]

    if string[0] == DOUBLE_QUOTES:
        string = string[1:]
        quotes = True
        terminators = [DOUBLE_QUOTES]
    elif string[0] == SINGLE_QUOTE:
        string = string[1:]
        quotes = True
        terminators = [SINGLE_QUOTE]

    for c in string:
        to_break = False
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
    return (Token_type.string, parsed, rest)


def lex_number(string):
    DIGITS = [str(d) for d in range(0, 10)]
    NUMBER_COMPONENTS = DIGITS + ["-", "."]

    token_type = None
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
        token_type = None
    elif string[0] != "\n":
        type, value, string = lex_string(string)
        return (type, parsed + value, string)
    elif "." in parsed:
        token_type = Token_type.float
        out = float(parsed)
    else:
        token_type = Token_type.int
        out = int(parsed)

    return (token_type, out, string) 


def lex_values(string, enum_inst):

    token = None
    out = None

    for key, value in enum_inst.value.items():
        if string.startswith(key):
            token = enum_inst
            out = value
            string = string[len(key) :]

            break

    return (token, out, string)



def tokenize(string):
    tokens = []


    while len(string) > 0:
        value = None

        fst_phase = [e for e in list(Token_type) if type(e.value) == dict]
        for i in fst_phase:
            toke_type, value, string = lex_values(string, i)
            if toke_type is not None:
                tokens.append((toke_type, value))
                break

        if toke_type is not None:
            continue
        
        funcs = [
            lex_number,
            lex_string,
        ]
        for func in funcs:
            toke_type, value, string = func(string)
            if toke_type is not None:
                tokens.append((toke_type, value))
                break

        if toke_type is not None:
            continue
        else:
            raise Exception("Unknown character")

    tokens.append((Token_type.end_of_file,))
    return tokens
