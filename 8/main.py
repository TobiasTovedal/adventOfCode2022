import re
import numpy as np

f = open("8/input.txt", "r")

for line in f:
    line = line.strip() # remove newline char
    line = re.split("", line)
    line.pop(-1)
    line.pop(0)

    arr = np.array(line)

    try: 
        mat = np.vstack([mat, arr])
    except:
        mat = arr

print(mat)

shape = mat.shape

for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        print(mat[i,j])