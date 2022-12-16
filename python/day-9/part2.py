import math


def getDistance(pointA, pointB):
    return math.sqrt(
        (pointB["x"] - pointA["x"]) ** 2 + (pointB["y"] - pointA["y"]) ** 2
    )


def getNewPositions(tailPosition, headPosition):

    newHeadPos = dict(headPosition)

    distance = getDistance(tailPosition, newHeadPos)

    if distance == 0 or distance == math.sqrt(2) or distance == 1:
        return tailPosition

    newTailPos = {key: value for key, value in tailPosition.items()}

    if tailPosition["y"] == newHeadPos["y"]:
        if tailPosition["x"] < newHeadPos["x"]:
            newTailPos["x"] += 1
        else:
            newTailPos["x"] -= 1

        return newTailPos

    if tailPosition["x"] == newHeadPos["x"]:
        if tailPosition["y"] < newHeadPos["y"]:
            newTailPos["y"] += 1
        else:
            newTailPos["y"] -= 1

        return newTailPos

    if distance == math.sqrt(8):
        possiblePositions = [
            {"x": tailPosition["x"] + 1, "y": tailPosition["y"] + 1},
            {"x": tailPosition["x"] - 1, "y": tailPosition["y"] + 1},
            {"x": tailPosition["x"] - 1, "y": tailPosition["y"] - 1},
            {"x": tailPosition["x"] + 1, "y": tailPosition["y"] - 1},
        ]

        for point in possiblePositions:
            if getDistance(point, headPosition) == math.sqrt(2):
                return point

    possiblePositions = [
        {"x": tailPosition["x"] + 1, "y": tailPosition["y"] + 1},
        {"x": tailPosition["x"] - 1, "y": tailPosition["y"] + 1},
        {"x": tailPosition["x"] - 1, "y": tailPosition["y"] - 1},
        {"x": tailPosition["x"] + 1, "y": tailPosition["y"] - 1},
    ]

    for point in possiblePositions:
        if getDistance(point, headPosition) == 1:
            return point


def moveKnots(knots, direction):

    if direction == "U":
        knots[0]["y"] += 1

    if direction == "D":
        knots[0]["y"] -= 1

    if direction == "R":
        knots[0]["x"] += 1

    if direction == "L":
        knots[0]["x"] -= 1

    for i in range(1, 10):

        knots[i] = getNewPositions(knots[i], knots[i - 1])


with open("input.txt") as f:
    line = f.readline()

    knots = [{"x": 0, "y": 0} for _ in range(10)]
    uniquePoints = {(0, 0)}

    while line:
        direction, times = line.split()
        times = int(times)

        for i in range(times):
            moveKnots(knots, direction)
            uniquePoints.add((knots[-1]["x"], knots[-1]["y"]))

        line = f.readline()

    print(len(uniquePoints))
