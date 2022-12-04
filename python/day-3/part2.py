with open("input.txt") as f:

    line = f.readline()

    sumOfPriorities = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters += letters.upper()

    while line:

        firstLine = line.strip()
        secondLine = f.readline().strip()
        thirdLine = f.readline().strip()

        for letter in firstLine:
            if letter in secondLine and letter in thirdLine:
                sumOfPriorities += letters.index(letter) + 1
                break

        line = f.readline()

    print(sumOfPriorities)
