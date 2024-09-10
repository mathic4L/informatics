from enum import Enum, auto

DOC_START = "---\n"
COLON = ":"
HYPHEN = "-"
LINE_BREAK = "\n"
SINGLE_QUOTE = '\''
DOUBLE_QUOTES = '\"'
SPACE = " "
ARR_START = "["
ARR_END = "]"

UNIT_INDENT = SPACE * 2
KEY_VALUE_DIV_ARR_OR_OBJ = COLON + LINE_BREAK
KEY_VALUE_DIV_SCALAR = COLON + SPACE
KEY_DIVS = [KEY_VALUE_DIV_ARR_OR_OBJ, KEY_VALUE_DIV_SCALAR]
ARRAY_MEMBER_QUALIFIER = HYPHEN + SPACE




class Token_type(Enum):

    string = auto()
    int = auto()
    float = auto()
    arr = auto()
    obj = auto() 

    bool = {"true": True, "false": False}
    null = {"null": None}

    arr_start = {"[": None}
    arr_end = {"]": None}
    doc_start = {DOC_START: DOC_START}
    end_of_file = auto()
    array_member_qualifier = {"- ": None}
    
    unit_indent = {UNIT_INDENT:None}
    line_break = {LINE_BREAK:None}

    colon_space = {": ":None}
    colon_linebreak = {":\n":None}
    # simple_end = {"\n":None}
    # obj_or_arr_end = auto()

