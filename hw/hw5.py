"""
1. При вводе строки целых положительных чисел, переменная int_seq
хранит отсортированный в порядке возрастания список

2. В цикле while выполняется проверка наличия в списке int_seq
переменной i. Проверка заканчивается в случае, если:
- переменная i входит в границы списка int_seq и при этом не ровна
элементам списка int_seq
- переменная i не входит в границы списка и равна int_seq[-1] + 1
"""

int_seq = sorted(set([int(x) for x in input("Enter  sequence: ").split()]))
i = 1
while i <= int_seq[-1]:
    if i not in int_seq:
        print(f"Result: {i}")
        break
    else:
        if i != int_seq[-1]:
            pass
        else:
            print(f"Result: {i + 1}")
    i += 1
