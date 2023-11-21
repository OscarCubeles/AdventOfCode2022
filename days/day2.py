ROCK_ME, PAPER_ME, SCISSORS_ME = 'X', 'Y', 'Z'
ROCK_OP, PAPER_OP, SCISSORS_OP = 'A', 'B', 'C'
VICTORY, DRAW, DEFEAT = 'Z', 'Y', 'X'
ROCK_PTS, PAPER_PTS, SCISSORS_PTS = 1, 2, 3

me_mapping = {ROCK_ME: 1, PAPER_ME: 2, SCISSORS_ME: 3}
result_mapping = {DEFEAT: 0, DRAW: 3, VICTORY: 6}

challenge1_mapping = {
    ROCK_OP: {ROCK_ME: 3, PAPER_ME: 6, SCISSORS_ME: 0},
    PAPER_OP: {ROCK_ME: 0, PAPER_ME: 3, SCISSORS_ME: 6},
    SCISSORS_OP: {ROCK_ME: 6, PAPER_ME: 0, SCISSORS_ME: 3}
}

challenge2_mapping = {
    ROCK_OP: {VICTORY: PAPER_PTS, DRAW: ROCK_PTS, DEFEAT: SCISSORS_PTS},
    PAPER_OP: {VICTORY: SCISSORS_PTS, DRAW: PAPER_PTS, DEFEAT: ROCK_PTS},
    SCISSORS_OP: {VICTORY: ROCK_PTS, DRAW: SCISSORS_PTS, DEFEAT: PAPER_PTS}

}


def day2():
    challenge1()
    challenge2()


def challenge1():
    totalScore = 0
    with open("./inputs/day2.txt", "r") as file:
        for line in file:
            opponent, me = line.split()
            totalScore += me_mapping[me]
            totalScore += challenge1_mapping[opponent][me]
    print(totalScore)


def challenge2():
    totalScore = 0
    with open("./inputs/day2.txt", "r") as file:
        for line in file:
            opponent, result = line.split()
            totalScore += result_mapping[result]
            totalScore += challenge2_mapping[opponent][result]
    print(totalScore)
