import numpy as np

f = open("3/input.txt", "r")

legend = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

sum = 0

def q(content):
    a = set(content[0:len(content)/2]) 
    b = set(content[-len(content)/2:len(content)])
    similar = a & b
    return(legend.index(list(similar)[0]) + 1)

def intersection3(a, b, c):
    return(list(a & b & c)[0])

lines = []

for line in f:
    content = list(line)
    try:
        content.remove("\n")
    except:
        print("eof")

    lines.append(content)
    
    # sum = sum + q(content)

i = 0

while i < len(lines)/3:
    j = i*3
    a = lines[j]
    b = lines[j + 1]
    c = lines[j + 2]
    i = i + 1
    sum = sum + legend.index((intersection3(set(a), set(b), set(c)))) + 1
    
print(sum)