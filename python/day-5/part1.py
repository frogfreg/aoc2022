with open("input.txt") as f:

    line = f.readline()
    rows = []

    while not line.replace(" ", "").replace("\n", "").isnumeric():

        line = line.replace("[", " ").replace("]", " ").replace("\n", "")

        rows.append(["0" if char.isspace() else char for char in line])

        line = f.readline()

    line = line.replace("\n", "")

    indexes = []
    stacks = []

    for index, letter in enumerate(line):
        if letter.isnumeric():
            indexes.append(index)

    for i in indexes:
        currenStack = []
        for row in rows:
            if row[i] != "0":
                currenStack.append(row[i])

        stacks.append(currenStack)

    line = f.readline()
    line = f.readline()

    while line:

        line = line.replace("move", "").replace("from", ",").replace("to", ",")

        quantity, origin, destiny = [int(num.strip()) for num in line.split(",")]

        for i in range(quantity):
            stacks[destiny - 1].insert(0, stacks[origin - 1].pop(0))

        line = f.readline()

    finalTop = ""

    for s in stacks:
        finalTop += s[0]

    print(finalTop)
