def draw(column, spriteCenter):
    newRow = False
    drawing = "!"

    if column >= 40:
        newRow = True
        column = 0

    if column in range(spriteCenter - 1, spriteCenter + 2):
        drawing = "#"
    else:
        drawing = "."

    return drawing, newRow


with open("input.txt", encoding="utf-8") as f:

    line = f.readline()
    cycleColumn = 0
    freq = 1
    rows = [[]]

    currentRowIndex = 0

    while line:

        line = line.removesuffix("\n")

        if line == "noop":

            drawing, newRow = draw(cycleColumn, freq)

            if newRow:
                rows.append([])
                currentRowIndex += 1
                cycleColumn = 0

            rows[currentRowIndex].append(drawing)
            cycleColumn += 1

        else:
            toAdd = int(line.split()[1])

            for i in range(2):

                drawing, newRow = draw(cycleColumn, freq)

                if newRow:
                    rows.append([])
                    currentRowIndex += 1
                    cycleColumn = 0

                rows[currentRowIndex].append(drawing)

                cycleColumn += 1

            freq += toAdd

        line = f.readline()

    for row in rows:
        print("".join(row))
