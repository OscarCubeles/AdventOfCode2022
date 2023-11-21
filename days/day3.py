def day3():
    # challenge1()
    challenge2()


def intersectStrings(str1, str2):
    common_chars = set(str1) & set(str2)
    return ''.join(common_chars).replace('\n', '')


def intersect3Strings(str1, str2, str3):
    intersection = set(str1) & set(str2) & set(str3)
    return ''.join(intersection).replace('\n', '')


def char_to_int(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27


def challenge1():
    totalPriority = 0
    with open("./inputs/day3.txt", "r") as file:
        for line in file:
            first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]
            cur_char = intersectStrings(first_half, second_half)
            totalPriority += char_to_int(cur_char)
    print(totalPriority)


def challenge2():
    total = 0
    with open("./inputs/day3.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            total += char_to_int(intersect3Strings(lines[i], lines[i+1], lines[i+2]))
    print(total)
