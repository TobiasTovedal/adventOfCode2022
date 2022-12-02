import numpy as np
import re

f = open("input.txt", "r")
elfs = np.array([])
elfIndex = 0
elfCalSum = 0

for line in f:
    if line != "\n":
        elfCalSum = elfCalSum + int(line)
    else:
        elfs = np.append(elfs, elfCalSum)
        elfCalSum = 0
        elfIndex = elfIndex + 1

print(np.sort(elfs))
print(71780 + 71481 + 69228)
