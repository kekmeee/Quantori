def countKollatza(number=int()):
    count = int()
    while number != 1:
        if number % 2 == 0 and number != 1:
            number //= 2
            count += 1
        else:
            number = number * 3 + 1
            count += 1
    return count

print(f"Count for 11: {countKollatza(11)}")
print(f"Count for 12: {countKollatza(12)}")
print(f"Count for 13: {countKollatza(13)}")
print(f"Count for 27: {countKollatza(27)}")
print(f"Count for 54: {countKollatza(54)}")
print(f"Count for 108: {countKollatza(108)}")
