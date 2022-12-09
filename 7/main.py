import re

class FileDictionary:
    def __init__(self, isFile, size, name, children):
        self.isFile = isFile
        self.size = size
        self.name = name
        self.children = children

    def addChild(self, child):
        self.children.append(child)

parentFile = FileDictionary(True, False, 0, "/", [], "none")

file = open("7/input.txt", "r")
listOfLines = []

for line in file:
    listOfLines.append(line.strip())

i = 0
while i < len(listOfLines):
    listOfLines[i] = re.split("\s+", line)
    
    if line[0] == "$" and line[1] == "cd":