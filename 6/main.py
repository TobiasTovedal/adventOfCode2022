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
    
