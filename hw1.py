"""
1. Составить таблицу соответствия между различными объектами основных классов: int, str и объектами класса bool.

|   Integer |   String  |   Bool    |
-------------------------------------
|     0     |   ""      |   False   |
-------------------------------------
|     1     |   " "     |  True     |
-------------------------------------
|   1345    |   asd     |  True     |
-------------------------------------
|    -1     |   \n      |  True     |
-------------------------------------

================================================

2. Разобраться с различиями между input() и raw_input(). Также в контексте разных версий python: 2 и 3.

Python2:
----------------
input():
Эквивалент eval(raw_input(prompt)).
При объявлении возвращает значение.
Пример:
> q = input()
> 2+3
> q
> 5
> z = eval(raw_input())
2+3
> z
5
----------------
raw_input():
При объявлении возвращает строку
Пример:
> w = raw_input()
2+3
> w
'2+3'


python3:
----------------
input():
При объявлении возвращает строку
Пример:
> a = input()
2+3
> a
'2+3'

================================================

3. Найти и прочитать PEP про изменение print между python2 и python3.

В python2 функция raw_input() была переименована и в python3 теперь это input().
"""

#  1 Задание
print("Integer 0: ", bool(0))
print("Integer 1: ", bool(1))
print("Integer 1345: ", bool(1345))
print("Integer -1: ", bool(-1))
print("String \"\": ", bool(""))
print("String \" \": ", bool(" "))
print("String asd: ", bool("asd"))
print("String newline (backward slash): ", bool("\n"))

