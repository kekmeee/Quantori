# Problem 6
print(f"Problem  6: {sum(x for x in range(1, 101)) ** 2 - sum(x ** 2 for x in range(1, 101))}")
# Problem 9
[print(f"Problem  9: {a * b * c}") for a in range(1, 1001) for b in range(1 + a, 1001 - a) for c in range(1, 1001 - a - b) if (a + b + c == 1000) and (a**2 + b**2 == c**2)]
# Problem 40
problem40 = [int("".join(str(i) for i in range(1, 185186))[j]) for j in [0, 9, 99, 999, 9999, 99999, 999999]]
res = 1
for i in problem40:
    res *= i
print(f"problem 40: {res}")
# Problem 48
print(f"Problem 48: {str(sum(x ** x for x in range(1, 1001)))[-10:-1]}")

