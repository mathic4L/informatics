# COMMA = ','
COLON = ":"
HYPHEN = "-"
# JSON_LEFTBRACKET = '['
# JSON_RIGHTBRACKET = ']'
# JSON_LEFTBRACE = '{'
LINE_BREAK = "\n"
DOUBLE_QUOTES = '"'
SPACE = " "

class Space:
    def __init__(self, count):
        self.count = count
        

MARKUP = [COLON, HYPHEN, SPACE] 
        #   JSON_LEFTBRACKET, JSON_RIGHTBRACKET,
#    JSON_LEFTBRACE, JSON_RIGHTBRACE]


DIGITS = [str(d) for d in range(0, 10)] + []
NUMBER_COMPONENTS = DIGITS + ["-", "."]

def parse_values(string):
    
    out = None
    
    if string == "null":
        return None
    elif string == "true":
        return True
    elif string == "false":
        return False
    elif isinstance(string, int):
        return int(string)
    elif isinstance(string, float):
        return float(string)
    else:
        return string


def parse_array(lines):
    size = len(lines)
    array = [None] * size

    default_prefix = lines[0].split(r"\w")[0]
    for line in lines:
        if line.startwith(default_prefix):
            line.lstrip(default_prefix)
        else:
            line.lstrip(default_prefix[0:-2] + "  ")

    for line in lines:


"""h
default_indent
current_el = 0
for line in lines
arr[current_el] = 

line = line.strip(default_indent)
if (!line.contains("-")):
    parse_simple(line)
elif line.startwith("-"):
    


"""

        

    
    # if "- value"
    array.append
    # if "- - value"
    

def get_size(lines):
    def get_indent(line):
        len(line) - len(line.strip())   

    indent_original = get_indent(lines[0])
    
    counter = 0
    for line in lines:
        current_indent = get_indent(line)
        if current_indent >= indent_original:
            counter += counter
        else:
            break
    
    return counter


def parse_object(tokens):
    json_object = {}
    t = tokens[0]

    if t == JSON_RIGHTBRACE:
        return json_object, tokens[1:]

    while True:
        json_key = tokens[0]

        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception("Expected key of type string")

        if tokens[0] != JSON_COLON:
            raise Exception("Expected colol ( : ) in object type dict")
        else:
            tokens = tokens[1:]

        json_value, tokens = parse(tokens)
        json_object[json_key] = json_value

        t = tokens[0]
        if t == JSON_RIGHTBRACE:
            return json_object, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception("Expected comma after pair in object, got: {}".format(t))
        tokens = tokens[1:]


def parse_all(tokens):
    t = tokens[0:1]
    if t == [LINE_BREAK, '''spaces''', HYPHEN]:
        return parse_array(tokens[1:])
    elif t == [LINE_BREAK]:
        return parse_object(tokens[1:])
    else:
        return t, tokens[1:]


def loads(string):
    return parse_all(parse(string))[0]
