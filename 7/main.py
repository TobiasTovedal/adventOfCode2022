import re

class File:
    def __init__(self,  isDir, name, size, children):
        self.isDir = isDir
        self.name = name
        self.size = size
        self.children = children

    def addChild(self, child):
        self.children.append(child)

def createFile(listOfLines):
    line = listOfLines[0]
    line = re.split("\s+", line)
    
    if line[0] == "$" and line[1] == "cd":
        file = File(True, line[2], 0, [])
        listOfLines.pop(0)

        for line in listOfLines:
            line = re.split("\s+", line)

            if line[2] != ".." and line[1] != "ls":
                if line[0] == "dir":
                    # create dir?
                else:
                    # create file
                print(line)
            
            elif line[2] == "..":
                print("breaking")
                break


    

f = open("7/input.txt", "r")
listOfLines = []

for line in f:
    listOfLines.append(line.strip())

createFile(listOfLines)
#print(listOfLines)