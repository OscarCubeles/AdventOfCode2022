def day4():
    challenge1()
    challenge2()


def challenge1():
    totalMatches = 0
    with open("./inputs/day4.txt", "r") as file:
        for line in file:
            low1, high1, low2, high2 = [int(x) for x in line.strip("\n").replace("-", ",").split(",")]
            if low1 <= low2 and high1 >= high2:
                totalMatches += 1
                continue
            if low2 <= low1 and high2 >= high1:
                totalMatches += 1
    print(totalMatches)


def challenge2():
    totalMatches = 0
    with open("./inputs/day4.txt", "r") as file:
        for line in file:
            low1, high1, low2, high2 = [int(x) for x in line.strip("\n").replace("-", ",").split(",")]
            if low1 <= low2 <= high1:
                totalMatches += 1
                continue
            if low2 <= low1 <= high2:
                totalMatches += 1
    print(totalMatches)

