def letters_range(start=str(), end=str(), step=1):
    result = [chr(x) for x in range(ord(start), ord(end), step)]
    return result
