import numpy as np

f = open("input.txt", "r")
values = np.array([])

for line in f:
    values = np.append(values, int(line))

for numOne in values:
    for numTwo in values:
        for numThree in values:
            if (numOne + numTwo + numThree == 2020):
                print(numOne * numTwo * numThree)

