# вариант 4
# Необходимо выбрать три любых буквы и расстояние между ними. С помощью
# регулярного выражения нужно найти все слова (последовательность символов
# ограниченная пробелами), в которых встречаются эти буквы в заданной
# последовательности и расстояние (например, через один друг от друга).

# буквы = {е, ц, я}
# расстояние = 1
# е_ц_я

test1 = "проекция"
test2 = "проекциия"
test3 = "проекц я"
test4 = "проекцция"
test5 = "хорошая проекция"

import re


def seq(string: str):
    antipattern = r"[^\sеця]"
    pattern = rf"\b{antipattern}*е{antipattern}ц{antipattern}я{antipattern}*\b"
    print(re.findall(pattern, string))


seq(test1) # ok
seq(test2)
seq(test3)
seq(test4)
seq(test5) # ok