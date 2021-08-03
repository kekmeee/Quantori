"""
Для удобства выполнения всех реализаций подается одна строка на вход
и разбивается элементы списка, считая пробел символом разделителя
"""
sequence = input("Enter  sequence: ").split()

"""
Решение, если не важен порядок.
Выводит на экран элементы множества, полученные из sequence.
"""
print("Answer №1: ", *set(sequence))

"""
Решение, если необходимо сохранить порядок, но не надо сохранять результат.
Выводит на экран элементы списка sequence.
"""
print("Answer №2: ", end=" ")
for i in range(len(sequence)):
    if sequence[i] not in sequence[0:i] or i == 0:
        print(sequence[i], end=" ")

"""
Решение, если необходимо сохранить порядок и надо сохранить результат
Выводит на экран элементы нового списка new_seq
"""
new_seq = []
for i in sequence:
    if i not in new_seq:
        new_seq.append(i)
print("\nAnswer №3: ", *new_seq, end="\n")
