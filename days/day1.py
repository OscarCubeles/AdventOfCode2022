def day1():
    challenge1()
    challenge2()


def challenge1():
    currTotal = 0
    maxCalories = 0
    with open("./inputs/day1.txt", "r") as file:
        for line in file:
            if line != "\n":
                currTotal += int(line)
            else:
                if maxCalories < currTotal:
                    maxCalories = currTotal
                currTotal = 0
    print(maxCalories)


def challenge2():
    currTotal = 0
    maxCalories = 0
    secondMax = 0
    thirdMax = -1
    with open("./inputs/day1.txt", "r") as file:
        for line in file:
            if line != "\n":
                currTotal += int(line)
            else:
                if maxCalories < currTotal:
                    aux = maxCalories
                    maxCalories = currTotal
                    thirdMax = secondMax
                    secondMax = aux
                    currTotal = 0
                    continue
                if secondMax < currTotal:
                    aux = secondMax
                    secondMax = currTotal
                    thirdMax = aux
                    currTotal = 0
                    continue
                if thirdMax < currTotal:
                    thirdMax = currTotal
                currTotal = 0
    print(thirdMax)
    print(secondMax)
    print(maxCalories)
    print(maxCalories + secondMax + thirdMax)
