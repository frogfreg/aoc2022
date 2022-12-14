import math

rows = []


def getScenicScore(rowIndex, columnIndex):
    scores = [0, 0, 0, 0]
    treeHeight = rows[rowIndex][columnIndex]

    for index in range(columnIndex - 1, -1, -1):

        if rows[rowIndex][index] < treeHeight:
            scores[0] += 1
            continue
        if rows[rowIndex][index] >= treeHeight:
            scores[0] += 1
            break

    for index in range(columnIndex + 1, len(rows[0])):
        if rows[rowIndex][index] < treeHeight:
            scores[1] += 1
            continue
        if rows[rowIndex][index] >= treeHeight:
            scores[1] += 1
            break

    columnHeights = [rows[i][columnIndex] for i in range(len(rows))]

    for index in range(rowIndex - 1, -1, -1):
        if columnHeights[index] < treeHeight:
            scores[2] += 1
            continue
        if columnHeights[index] >= treeHeight:
            scores[2] += 1
            break

    for index in range(rowIndex + 1, len(columnHeights)):
        if columnHeights[index] < treeHeight:
            scores[3] += 1
            continue
        if columnHeights[index] >= treeHeight:
            scores[3] += 1
            break

    return math.prod(scores)


with open("input.txt") as f:

    line = f.readline()

    while line:

        line = line.removesuffix("\n")

        rows.append([int(digit) for digit in line])

        line = f.readline()

scores = []

for rowIndex in range(len(rows)):
    for colIndex in range(len(rows[0])):
        scores.append(getScenicScore(rowIndex, colIndex))

print(max(scores))
