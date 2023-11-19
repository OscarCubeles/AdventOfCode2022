def day1():
    challenge1()
    #challenge2()


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
    f = open("/days/day1.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
    f.close()