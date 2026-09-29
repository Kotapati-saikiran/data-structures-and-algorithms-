def search(chars):
    i = 0
    j = 1
    write = 0
    count = 1

    while j < len(chars):
        if chars[i] == chars[j]:
            count += 1
            j += 1

        else:
            chars[write] = chars[i]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            i = j
            j += 1
            count = 1

    chars[write] = chars[i]
    write += 1

    if count > 1:
        for digit in str(count):
            chars[write] = digit
            write += 1
    return write


chars = ["a", "a", "b", "b", "c", "c", "c"]
print(search(chars))
print(chars)