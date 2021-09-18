def checkNumberString(string, length=0):
    if string == "":  # проверка не пустой строки
        return False
    else:
        if length < len(string):  # условие выхода из функции при проходе по всей строке
            if string[length].isdigit():  # проверка символа на число, в случае True проверяем следующий символ
                return checkNumberString(string, length + 1)
            else:
                return False
        else:
            return True


while True:
    seq = input("Enter sequence: ")
    if seq == "cancel":
        print("Bye!")
        exit()
    elif not checkNumberString(seq):
        print("Не удалось преобразовать введенный текст в число.")
    else:
        if int(seq) % 2 == 0:
            print(int(seq) // 2)
        else:
            print(int(seq) * 3 + 1)
