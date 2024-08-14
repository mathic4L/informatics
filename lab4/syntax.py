from enum import Enum
class json(Enum):
    obj_start = "{"
    obj_end = "}"
    arr_start = "["
    arr_end = "]"
    colon = ":"
    line_break = "\n"
    quot_mark = "\""


class token:
    def __init__(self, type: json, content):
        self.type = type
        self.content = content
    