number = int(input("Enter number: "))
count = int()
while number != 1:
    if number % 2 == 0 and number != 1:
        number //= 2
        count += 1
    else:
        number = number * 3 + 1
        count += 1
print(count)
