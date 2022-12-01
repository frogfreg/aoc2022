calories = []

with open("input.txt") as f:
    line = f.readline()

    currentCalories = 0

    while line:
        if line.strip() == "":
            calories.append(currentCalories)
            line = f.readline()
            currentCalories = 0
            continue

        currentCalories += int(line.strip())
        line = f.readline()

    calories.append(currentCalories)

    calories.sort()

    print(sum(calories[-3:]))
