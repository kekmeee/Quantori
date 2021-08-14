def letters_range(start, end, step=1):
    result = [chr(x) for x in range(ord(start), ord(end), step)]
    return result
