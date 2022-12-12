import re

import numpy as np

 

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

def averagePositions(positions):
    xPos = 0
    yPos = 0

    for position in positions:
        xPos += position[0]
        yPos += position[-1]

    return [int(round(xPos/len(positions), 0)), int(round(yPos/len(positions), 0))]


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

for move in moves:
    head.move(move)

    headPosition = head.getPosition()
    tailPosition = tail.getPosition()

    #overlappingPositions = []

    if headPosition not in tail.getFootprint():
        xMove = int(round(0.5 * (tailPosition[0] - headPosition[0]), 0))
        yMove = int(round(0.5 * (tailPosition[-1] - headPosition[-1]), 0))

        tail.move([xMove, yMove])
        #print(tail.getFootprint())

        #for position in tail.getFootprint():

        #    if position in head.getFootprint():

        #        overlappingPositions.append(position)

           

        #print(averagePositions(overlappingPositions))

        #tail.move(averagePositions(overlappingPositions))


    print(tail.getPosition())