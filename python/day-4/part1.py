with open("input.txt") as f:

    overlapCounter = 0

    line = f.readline()

    while line:

        firstPair, secondPair = line.strip().split(",")
        firstLow, firstUpper = [int(num) for num in firstPair.split("-")]
        secondLow, secondUpper = [int(num) for num in secondPair.split("-")]

        if firstLow <= secondLow and firstUpper >= secondUpper:

            overlapCounter += 1
        elif secondLow <= firstLow and secondUpper >= firstUpper:

            overlapCounter += 1

        line = f.readline()

    print(overlapCounter)
