# вариант = 5,1,3
# глаза = [
# нос = -
# рот = |
# [-|

import re

target = "[-|" 
test_empty = f"" # 0 
test_single = f"it's a {target} world" # 1
test_multiple = f"world: hello {target}! {target}: hello world!" # 2
test_spaced = f"hello world, [- | said" # 0
test_wrong_emotion = f"hello world [-)" # 0

def get_count(string):
    count = len(re.findall(r"\[-\|", string))
    print(count)

get_count(test_empty)
get_count(test_single)
get_count(test_multiple)
get_count(test_spaced)
get_count(test_wrong_emotion)



