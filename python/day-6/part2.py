text = ""

with open("input.txt") as f:
    text = f.readline()

currentIndex = 13

letters = [*text[:14]]

while len(set(letters)) < 14:
    currentIndex += 1

    letters.pop(0)
    letters.append(text[currentIndex])

print(currentIndex + 1)
