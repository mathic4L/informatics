from gramatics import *
import re

def lex_string(string):
    quotes = False
    terminator = r'[:\n]'

    if string[0] == '"':
        quotes = True
        terminator = [DOUBLE_QUOTES]
        string = string[1:]  # Удаляем начальную кавычку
    elif string[0] == "'":
        quotes = True
        terminator = [SINGLE_QUOTE]
        string = string[1:]  # Удаляем начальную кавычку

    if quotes:
        match = re.match(f'^[^{terminator}]*', string)
        if match:
            parsed = match.group(0)
            rest = string[len(parsed) + 1:]  # Пропускаем закрывающую кавычку
        else:
            parsed = ""
            rest = string
    else:
        # Регулярное выражение для строки до терминатора (двоеточие или новая строка)
        match = re.match(r'^[^:\n]*', string)
        if match:
            parsed = match.group(0)
            rest = string[len(parsed):]
        else:
            parsed = ""
            rest = string

    return (Token_type.string, parsed, rest)


def lex_number(string):
    token_type = None
    number_regex = r'^-?\d+(\.\d+)?'
    
    match = re.match(number_regex, string)
    
    if not match:
        return (None, None, string)
    
    parsed = match.group(0)
    string = string[len(parsed):]

    if "." in parsed:
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
