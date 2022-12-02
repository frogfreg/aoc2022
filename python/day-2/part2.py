with open("input.txt") as f:
    score = 0

    line = f.readline()

    value = {"A": 1, "B": 2, "C": 3}
    winsCases = {"A": "C", "B": "A", "C": "B"}
    loseCases = {"C": "A", "A": "B", "B": "C"}
    resultValue = {"X": 0, "Y": 3, "Z": 6}

    while line:

        line = line.replace("\n", "")

        rivalChoice = line[0]
        result = line[-1]

        choiceScore = 0

        if result == "Y":
            choiceScore = value[rivalChoice]
        if result == "X":
            choiceScore = value[winsCases[rivalChoice]]
        if result == "Z":
            choiceScore = value[loseCases[rivalChoice]]

        score += resultValue[result] + choiceScore

        line = f.readline()

    print(score)
