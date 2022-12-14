class Node:
    def __init__(self, name, size=0, isDir=False, kids=[]):
        self.size = size
        self.isDir = isDir
        self.kids = kids
        self.name = name

    def getSize(self):
        if self.isDir == False:
            return self.size

        currSize = sum([node.getSize() for node in self.kids])

        return currSize


root = Node(20, False, [])


print(root.getSize())
