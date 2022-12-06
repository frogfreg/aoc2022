text = ""

with open("input.txt") as f:
    text = f.readline()

currentIndex = 3

letters = [*text[:4]]

while len(set(letters)) < 4:
    currentIndex += 1

    letters.pop(0)
    letters.append(text[currentIndex])

print(currentIndex + 1)
