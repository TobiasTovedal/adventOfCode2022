import re


f = open("7/input.txt", "r")
listOfLines = []
graph = {}
visited = set()
id = 0
directorySizes = {}
currentKeyStack = []

for line in f:
    listOfLines.append(line.strip())

# Create tree
for line in listOfLines:
    line = re.split("\s+", line)

    if line[0] == "$" and line[1] == "cd":
        if line[2] != "..":
            currentKeyStack.append(line[2] + str(id))
            graph[currentKeyStack[-1]] = []
            directorySizes[currentKeyStack[-1]] = 0
            id += 24332

        else:
            currentKeyStack.pop()
    
    if line[0] == "dir":
        graph[currentKeyStack[-1]].append(line[1])

    if line[0] != "dir" and line[0] != "$":
        graph[currentKeyStack[-1]].append(int(line[0]))

        for directory in currentKeyStack:
            directorySizes[directory] += int(line[0])
        

maxSizeDirectory = 0
for directory in directorySizes:
    if directorySizes[directory] > maxSizeDirectory:
        maxSizeDirectory = directorySizes[directory]

largeDirectories = {}
for directory in directorySizes:
    #print(directory)
    if directorySizes[directory] >= (30000000-(70000000 - maxSizeDirectory)):
        #print(directorySizes[directory])
        largeDirectories[directory] = directorySizes[directory]

smallest = 70000000
for directory in largeDirectories:
    if largeDirectories[directory] < smallest:
        smallest = largeDirectories[directory]

#print(maxSizeDirectory)
#print(70000000 - maxSizeDirectory)
print(smallest)