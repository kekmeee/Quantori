sequence = input("Enter  sequence: ")
result = 0
i = 0
while i < len(sequence):
    s = ""
    if sequence[i] == "-" or sequence[i].isnumeric():
        s += sequence[i]
        i += 1
        while i < len(sequence) and sequence[i].isnumeric():
            s += sequence[i]
            i += 1
    if s != "":
        result += int(s)
    i += 1
print(result)
