from enum import Enum, auto

DOC_START = "---\n"
COLON = ":"
HYPHEN = "-"
LINE_BREAK = "\n"
DOUBLE_QUOTES = '"'
SPACE = " "
ARR_START = "["
ARR_END = "]"

SINGLE_INDENT = SPACE * 2
KEY_VALUE_DIV_ARR_OR_OBJ = COLON + LINE_BREAK
KEY_VALUE_DIV_SCALAR = COLON + SPACE
KEY_DIVS = [KEY_VALUE_DIV_ARR_OR_OBJ, KEY_VALUE_DIV_SCALAR]

ARRAY_MEMBER_QUALIFIER = HYPHEN + SPACE

MARKUP = [
    ARR_START,
    ARR_END,
    DOC_START,
    ARRAY_MEMBER_QUALIFIER,
    KEY_VALUE_DIV_ARR_OR_OBJ,
    KEY_VALUE_DIV_SCALAR,
    SINGLE_INDENT,
    LINE_BREAK,
]


class Token_type(Enum):

    string = auto(),
    int = auto(),
    float = auto(),
    bool = auto(),
    null = auto(),
    
    arr_start = auto()
    arr_end = auto()
    doc_start = auto()
    array_member_qualifier = auto(),
    simple_start = auto(),
    simple_end = auto(),
    single_indent = auto(),
    line_break = auto()

    obj_or_arr_start = auto()
    obj_or_arr_end = auto()
