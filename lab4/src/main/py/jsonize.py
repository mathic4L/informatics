from util import *


def jsonize(d):

    if not isinstance(d, dict):
        raise TypeError("{exception_prefix}Input must be a dictionary")

    return serialize_dict(d)


def serialize_value(value):
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, dict):
        return serialize_dict(value)
    elif isinstance(value, list):
        return serialize_list(value)
    else:
        raise TypeError(f"{exception_prefix}Unsupported data type")


def serialize_dict(d):
    items = [
        f"{serialize_value(key)}: {serialize_value(value)}" for key, value in d.items()
    ]
    return f'{{{", ".join(items)}}}'


def serialize_list(lst):
    items = [serialize_value(item) for item in lst]
    return f'[{", ".join(items)}]'
