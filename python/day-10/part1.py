with open("input.txt", encoding="utf-8") as f:

    line = f.readline()

    cycles = 0

    freq = 1

    twentyFriends = list(range(20, 221, 40))
    signals = []

    while line:

        line = line.removesuffix("\n")

        if line == "noop":
            cycles += 1
            toAdd = 0
        else:
            toAdd = int(line.split()[1])
            cycles += 2

        if cycles - 1 in twentyFriends and line != "noop":

            signals.append((cycles - 1) * freq)

        if cycles in twentyFriends:

            signals.append(cycles * freq)

        freq += toAdd
        line = f.readline()

    print(sum(signals))
