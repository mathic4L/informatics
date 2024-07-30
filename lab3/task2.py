# вариант 5
# С помощью регулярного выражения найти в тексте все слова, в которых две гласные
# стоят подряд, а после этого слова идёт слово, в котором не больше 3 согласных.

import re

test1 = "красивые поля, чистое небо" #2
test2 = "красивую звезду над нами" #1
test3 = "я вижу уникальную идею в ярком небе" #1
test4 = "эта ситуация исключительна важна" #1
test5 = "прекрасный мир открылся перед нами" #0

def words(string: str):
    glasnie = "[ауоиэыяюеё]"
    soglasnie= "[бвгджзйклмнпрстфхцчшщ]"
    # anything = rf"(?:{soglasnie}*{glasnie}*)"
    first_word = rf"\b\w*?{glasnie}{{2}}\w*\b " 
    second_word = rf"\b\w+?(?:{glasnie}*{soglasnie}{{1}}{glasnie}*){{0,3}}\b"
    print(re.findall(first_word + second_word, string))

words(test1)
words(test2)
words(test3)
words(test4)
words(test5)
