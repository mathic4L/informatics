#   \n -> {
# \n -> }
# str -> "string"
# false/true -> false/true
# number -> number

# indexnt < 0 -> }
# abc: ->
# abc:
#     abc: -> {
# abc:
#   - ... -> [

from syntax import token
from syntax import json

def yaml_parser(src: str, seq: str):
    if src.startswith(seq):
        src = src[len(seq):]


def cb_appender(src: str):


def from_yaml(src: str):
    out = []
    src = src.split("\n")
    indent_delta = 0
    for index in range():
        
        line = src[index].strip()
        indent_delta = len(src[index]) - len(line) - indent_delta

        key, value = line.split(": ")
        if(value != ""):
            sdf
        else:
            if("-" in src[index + 1]):
                

        if(abs(indent_delta) != 0):
            token = json.obj_start if indent_delta > 0 else json.obj_end
            for time in range(abs(indent_delta)):
                out.append(token)
        if ()
        # append braces
        
    

    # append braces
        
        
   
    return out

def to_json():
    # 
    # {...}
    return ""

def func(src: str):
    lines = src.split('\n')
    out = []
    for line in lines:
        print()


