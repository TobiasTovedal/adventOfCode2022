import numpy as np
import re

f = open("2/input.txt", "r")
me = np.array([])
you = np.array([])

for line in f:
    play = line.split()
    you = np.append(you, play[0])
    me = np.append(me, play[1])


j = 0
score = 0
while j < len(me):
    # Lose
    if me[j] == "X":
        if you[j] == "A":
            score = score + 3
        if you[j] == "B":
            score = score + 1
        if you[j] == "C":
            score = score + 2
    
    # Draw
    if me[j] == "Y":
        score = score + 3
        if you[j] == "A":
            score = score + 1
        if you[j] == "B":
            score = score + 2
        if you[j] == "C":
            score = score + 3
    
    # Win
    if me[j] == "Z":
        score = score + 6
        if you[j] == "A":
            score = score + 2
        if you[j] == "B":
            score = score + 3
        if you[j] == "C":
            score = score + 1
    
    j = j + 1

"""
i = 0
score = 0
while i < len(you):
    if me[i] == "X":
        score = score + 1
        if you[i] == "A":
            score = score + 3
        if you[i] == "C":
            score = score + 6
    if me[i] == "Y":
        score = score + 2
        if you[i] == "B":
            score = score + 3
        if you[i] == "A":
            score = score + 6
    if me[i] == "Z":
        score = score + 3
        if you[i] == "C":
            score = score + 3
        if you[i] == "B":
            score = score + 6
    
    i = i + 1
"""

print(score)