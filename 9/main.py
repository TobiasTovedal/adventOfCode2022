import re
class RopeEnd:
    position = [0, 0]

    def __init__(self, startPosition):
        self.position = startPosition

    def move(self, movement):
        self.position[0] = self.position[0] + movement[0]
        self.position[-1] = self.position[-1] + movement[-1]

    def getPosition(self):
        return self.position

    def getFootprint(self):
        footprint = []

        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                footprint.append([self.position[0] + x, self.position[-1] + y])

        return footprint

f = open("9/input.txt", "r")
moves = []

for line in f:
    line = line.strip()
    line = list(line)

    if line[0] == "R":
        for step in range(int(line[-1])):
            moves.append([1, 0])

    elif line[0] == "L":
        for step in range(int(line[-1])):
            moves.append([-1, 0])

    elif line[0] == "U":
        for step in range(int(line[-1])):
            moves.append([0, 1])

    else:
        for step in range(int(line[-1])):
            moves.append([0, -1])

head = RopeEnd([0, 0])
tail = RopeEnd([0, 0])
visitedPositions = {"[0, 0]"}
lastDirectionFromPosition = [0, 0]

for move in moves:
    head.move(move)

    headPosition = head.getPosition()
    tailPosition = tail.getPosition()

    for i in [0, -1]:
            if headPosition[i] > tailPosition[i]:
                lastDirectionFromPosition[i] = 1
            elif headPosition[i] < tailPosition[i]:
                lastDirectionFromPosition[i] = -1
            else:
                lastDirectionFromPosition[i] = 0

    if abs(headPosition[0] - tailPosition[0]) > 1 or abs(headPosition[-1] - tailPosition[-1]) > 1:
        tail.move(lastDirectionFromPosition)
        visitedPositions.add(str(tail.getPosition()))

    print("Head: " + str(head.getPosition()) + ", Tail: " + str(tail.getPosition()))

print(len(visitedPositions))
