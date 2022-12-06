<<<<<<< HEAD
file = open("6/input.txt", "r")

def finder(line):
    packetLength = 14
    i = 0
    while i < len(line) - packetLength:
        marker = line[i:i+packetLength] 
        numberOfOccurances = 0

        for character in marker:
            numberOfOccurances = numberOfOccurances + marker.count(character)
        
        if numberOfOccurances == packetLength: 
            print(marker, i + packetLength) 
            break

        i = i + 1

for line in file:
    finder(line)
    
=======
import re

f = open("5/input.txt", "r")
v = [[],[],[],[],[],[],[],[],[]]
moves = []

i = 0
for line in f:
    if i < 8:
        line = list(line)
        if line[1].isalpha():
            v[0].insert(0, line[1])
        
        if line[5].isalpha():
            v[1].insert(0, line[5])

        if line[9].isalpha():
            v[2].insert(0, line[9])
        
        if line[13].isalpha():
            v[3].insert(0, line[13])
        
        if line[17].isalpha():
            v[4].insert(0, line[17])
        
        if line[21].isalpha():
            v[5].insert(0, line[21])
        
        if line[25].isalpha():
            v[6].insert(0, line[25])
        
        if line[29].isalpha():
            v[7].insert(0, line[29])
        
        if line[33].isalpha():
            v[8].insert(0, line[33])

    if i > 9:
        line = re.findall(r"\d+", line) # split line str into list of vals
        moves.append(line)
    
    i = i + 1

### pt 1
#for move in moves:
#    print(l)
#    for x in range(int(move[0])):
#        v[int(move[-1]) - 1].append(v[int(move[1]) - 1][-1])
#        v[int(move[1]) - 1].pop()
#    print(move)

### pt 2
for move in moves:
    l = len(v[int(move[-1]) - 1])
    print(l)
    for x in range(int(move[0])):
        v[int(move[-1]) - 1].insert(l, v[int(move[1]) - 1][-1])
        v[int(move[1]) - 1].pop()
    print(move)

print(v)
>>>>>>> 51b02a76e5202bdbd2e136e97c6bb4d7d63a7156
