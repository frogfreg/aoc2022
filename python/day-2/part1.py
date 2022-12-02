with open("input.txt") as f:
    score = 0

    line = f.readline()
    wins = {"A": "Z", "B": "X", "C": "Y", "X": "C", "Y": "A", "Z": "B"}
    value = {"X": 1, "Y": 2, "Z": 3}

    while line:

        line = line.replace("\n", "")

        rivalChoice = line[0]
        myChoice = line[-1]
        matchResult = 3

        if wins[myChoice] == rivalChoice:
            matchResult = 6

        if wins[rivalChoice] == myChoice:
            matchResult = 0

        score += value[myChoice] + matchResult

        line = f.readline()

    print(score)
