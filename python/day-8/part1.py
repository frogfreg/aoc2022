rows = []


def isVisible(rowIndex, columnIndex):

    treeHeight = int(rows[rowIndex][columnIndex])

    if treeHeight > max(rows[rowIndex][:columnIndex]) or treeHeight > max(
        rows[rowIndex][columnIndex + 1 :]
    ):
        return True

    columnNums = []

    for i in range(len(rows)):
        columnNums.append(rows[i][columnIndex])

    if treeHeight > max(columnNums[:rowIndex]) or treeHeight > max(
        columnNums[rowIndex + 1 :]
    ):
        return True

    return False


with open("input.txt") as f:

    line = f.readline()

    while line:

        line = line.removesuffix("\n")

        rows.append([int(digit) for digit in line])

        line = f.readline()

visible = len(rows[0]) + len(rows[-1]) + len(rows[1:-1]) * 2

for rowIndex in range(len(rows)):
    if rowIndex == 0 or rowIndex == len(rows) - 1:
        continue

    for columnIndex in range(len(rows[0])):
        if columnIndex == 0 or columnIndex == len(rows[0]) - 1:
            continue

        if isVisible(rowIndex, columnIndex):
            visible += 1


print(visible)
