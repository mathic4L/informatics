from data_parsers import (
    parse_number,
    parse_string,
    parse_bool,
    parse_null,
    parse_object,
    parse_array,
    parse_values,
    get_size
)

def parse_obj(string):
    current_indent = 0
    obj = {}
    lines = string.split("\n")
    counter = 0
    lines_len = len(lines)
    while(counter, lines_len):
        key, value = lines[counter].split(":")
        value = value.strip()
        if value == "":  # obj
            sub_array = lines[counter + 1: counter + 1 + get_size(counter + 1)]
            obj[key] = parse_obj(sub_array)
        if value == "":  # arr
            sub_array = lines[counter + 1: counter + 1 + get_size(counter + 1)]
            obj[key] = parse_array(sub_array)
        else:  # simple value
            obj[key] = parse_values(value)

    return obj


yaml = """hello: hello
world: world
!: !"""  # переносы строк сохраняются в значении строги в отличие от других языков

print(parse_obj(yaml))

[].