import re
import numpy as np

f = open("8_mac/input.txt", "r")

for line in f:
    line = line.strip()
    line = list(line)

    arr = np.array(line)

    try:
        mat = np.vstack([mat, arr])
    except:
        mat = arr

print(mat)

shape = mat.shape


def checkNeighbours(mat, currentRow, currentColumn):
    numberOfShadowingTrees = 0
    scenicScore = [0, 0, 0 ,0]

    for row in range(currentRow+1, mat.shape[0]):
        scenicScore[0] = scenicScore[0] + 1
        if mat[row, currentColumn] >= mat[currentRow, currentColumn]:
            numberOfShadowingTrees = numberOfShadowingTrees + 1
            break
    
    for row in range(currentRow-1, -1, -1):
        scenicScore[1] = scenicScore[1] + 1
        if mat[row, currentColumn] >= mat[currentRow, currentColumn]:
            numberOfShadowingTrees = numberOfShadowingTrees + 1
            break

    for col in range(currentColumn+1, mat.shape[1]):
        scenicScore[2] = scenicScore[2] + 1
        if mat[currentRow, col] >= mat[currentRow, currentColumn]:
            numberOfShadowingTrees = numberOfShadowingTrees + 1
            break
        
    for col in range(currentColumn-1, -1, -1):
        scenicScore[3] = scenicScore[3] + 1
        if mat[currentRow, col] >= mat[currentRow, currentColumn]:
            numberOfShadowingTrees = numberOfShadowingTrees + 1
            break
    
    return numberOfShadowingTrees, np.prod(scenicScore)

isVisible = np.zeros(shape)
matrixScenicScore = np.zeros(shape)
nVisibleTrees = 0
scenicScoreTop = 0

for row in range(mat.shape[0]):
    for col in range(mat.shape[1]):
        nShadowTrees, scenicScore = checkNeighbours(mat, row, col)

        matrixScenicScore[row, col] = scenicScore

        if nShadowTrees < 4:
            isVisible[row, col] = 1
            nVisibleTrees = nVisibleTrees + 1
        
        if scenicScore > scenicScoreTop:
            scenicScoreTop = scenicScore


print(matrixScenicScore)
print(scenicScoreTop)
