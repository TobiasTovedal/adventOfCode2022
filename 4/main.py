import re

f = open("4/input.txt", "r")
i = 0

for line in f:
    line = line.strip() # remove newline char
    line = re.split("\D", line) # split line str into list of vals

    set1 = set(range(int(line[0]), int(line[1]) + 1))
    set2 = set(range(int(line[2]), int(line[3]) + 1))

    ## 1 part
    #if set1 | set2 == set1 or set1 | set2 == set2:
    #   i = i + 1

    ## 2 part
    if len(set1 & set2) > 0:
        i = i + 1

print(i)