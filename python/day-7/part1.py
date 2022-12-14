class Node:
    def __init__(self, name, size=0, isDir=False, kids=[], parent=None):
        self.name = name
        self.size = size
        self.isDir = isDir
        self.kids = kids
        self.parent = parent

    def getSize(self):
        if self.isDir == False:
            return self.size

        currSize = sum([node.getSize() for node in self.kids])

        return currSize


with open("input.txt") as f:

    line = f.readline()
    line = f.readline()
    line = f.readline()

    root = Node("/", 0, True, [])

    currentNode = root
    dirs = [root]

    while line:

        if line.startswith("dir"):
            newNode = Node(line.split()[1], 0, True, [], currentNode)
            currentNode.kids.append(newNode)
            dirs.append(newNode)

        if line.split()[0].isnumeric():
            size, filename = line.split()

            currentNode.kids.append(Node(filename, int(size), False, [], currentNode))

        if line.startswith("$ cd"):

            dirname = line.split()[2]

            if dirname != "..":

                for node in currentNode.kids:
                    if node.name == dirname:
                        currentNode = node
                        break

            if dirname == "..":
                currentNode = currentNode.parent

        line = f.readline()

    dirSizes = [dir.getSize() for dir in dirs]

    print(sum([size for size in dirSizes if size < 100_000]))
