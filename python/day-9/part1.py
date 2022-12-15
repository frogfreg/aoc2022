import math


def getDistance(pointA, pointB):
    return math.sqrt(
        (pointB["x"] - pointA["x"]) ** 2 + (pointB["y"] - pointA["y"]) ** 2
    )


def getNewPositions(tailPosition, headPosition, direction):

    newHeadPos = dict(headPosition)

    if direction == "U":
        newHeadPos["y"] += 1

    if direction == "D":
        newHeadPos["y"] -= 1

    if direction == "R":
        newHeadPos["x"] += 1

    if direction == "L":
        newHeadPos["x"] -= 1

    distance = getDistance(tailPosition, newHeadPos)

    if distance == 0 or distance == math.sqrt(2) or distance == 1:
        return tailPosition, newHeadPos

    newTailPos = {key: value for key, value in tailPosition.items()}

    if tailPosition["y"] == newHeadPos["y"]:
        if tailPosition["x"] < newHeadPos["x"]:
            newTailPos["x"] += 1
        else:
            newTailPos["x"] -= 1

        return newTailPos, newHeadPos

    if tailPosition["x"] == newHeadPos["x"]:
        if tailPosition["y"] < newHeadPos["y"]:
            newTailPos["y"] += 1
        else:
            newTailPos["y"] -= 1

        return newTailPos, newHeadPos

    if distance == math.sqrt(5):
        return headPosition, newHeadPos


with open("input.txt") as f:
    line = f.readline()

    tail, head = {"x": 0, "y": 0}, {"x": 0, "y": 0}
    uniquePoints = {(0, 0)}

    while line:
        direction, times = line.split()
        times = int(times)

        for i in range(times):
            tail, head = getNewPositions(tail, head, direction)
            uniquePoints.add((tail["x"], tail["y"]))

        line = f.readline()

    print(len(uniquePoints))
