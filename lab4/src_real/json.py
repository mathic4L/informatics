from enum import Enum, auto

SPACE = " "


class Type(Enum):
    NULL = auto()
    BOOL = auto()
    INT = auto()
    FLOAT = auto()
    STR = auto()
    ARR = auto()
    OBJ = auto()

    def to_type(input):
        types = {
            type(None): Type.NULL,
            bool: Type.BOOL,
            int: Type.INT,
            float: Type.FLOAT,
            str: Type.STR,
            type([]): Type.ARR,
            type({}): Type.OBJ,
        }
        for key, value in types.items():
            if isinstance(input, key):
                return value


class Json:

    def __init__(self, data_type, data):
        self._data, self._data_type = data, data_type
    
    def convert(obj):
        return "{\n" + SPACE * 4 + Json.create(obj).to_string() + "\n}"

    def create(obj):
        data_type = Type.to_type(obj)
        data = obj
        if data_type == Type.ARR:
            data = [Json.create(val) for val in obj]
        elif data_type == Type.OBJ:
            data = dict((key, Json.create(val)) for (key, val) in obj.items())
        return Json(data_type, data)

    def to_string(self, tabs=0, prefix=""):
        def pre(tabs):
            return "  " * tabs

        if (self._data_type == Type.ARR or self._data_type == Type.OBJ) and len(
            self._data
        ) == 0:
            return "[]" if self._data_type == Type.ARR else "{}"
        elif self._data_type == Type.ARR:
            return (
                ""
                if tabs == 0
                else "\n"
                + "\n".join(
                    [
                        "{}- {}".format(pre(tabs - 1), val.to_string(tabs))
                        for val in self._data
                    ]
                )
                + "\n"
            )
        elif self._data_type == Type.OBJ:
            return "\n{}".format(pre(tabs)).join(
                [
                    (
                        "{}:\n{}{}".format(
                            key, pre(tabs + 1), val.to_string(tabs + 1, prefix=" ")
                        )
                        if (val._data_type == Type.OBJ)
                        else "{}:{}".format(key, val.to_string(tabs + 1, prefix=" "))
                    )
                    for (key, val) in self._data.items()
                ]
            )
        elif self._data_type == Type.NULL:
            return prefix + "null"
        elif self._data_type == Type.STR:
            if len(self._data.split("\n")) > 1:
                return " |\n" + "\n".join(
                    pre(tabs + 1) + val for val in self._data.split("\n")
                )
            else:
                return prefix + self._data
        else:
            return prefix + str(self._data)
