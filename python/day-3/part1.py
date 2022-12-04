with open("input.txt") as f:
    line = f.readline()

    sumOfPriorities = 0

    letters = "abcdefghijklmnopqrstuvwxyz"
    letters += letters.upper()

    while line:
        line = line.strip()
        firstCompartment = line[: len(line) // 2]
        secondCompartment = line[len(line) // 2 :]

        common = ""

        for letter in firstCompartment:
            if letter in secondCompartment:
                common = letter
                break

        sumOfPriorities += letters.index(common) + 1
        line = f.readline()

    print(sumOfPriorities)
