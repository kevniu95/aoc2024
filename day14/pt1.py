import re
import csv

def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def initGrid(gridCols: int, gridRows: int):
    grid = []
    for row in range(gridRows):
        gridRow = [0 for col in range(gridCols)]
        grid.append(gridRow)
    return [gridRow for gridRow in grid]
            
def initBotDict(inputArray: list[str]) -> dict[int, tuple[list[int, int], tuple[int, int]]]:
    '''
    Returns a 'bot dict' where each: 
        key: original position of bot in input Array
        value: Tuple of tuples
            First tuple - current position
            Second tuple - velocity
    '''
    botsIndex = 0
    botDict = {}
    for line in inputArray:
        if line.startswith('p'):
            py, px = re.search(r"p[\=]([-,0-9]*)", line).group(1).split(',')
            vy, vx = re.search(r"v[\=]([-,0-9]*)", line).group(1).split(',')
            botDict[botsIndex] = [[int(px), int(py)], (int(vx), int(vy))]
            botsIndex += 1
    return botDict

def correctGridValue(x: int, dimensionCount: int):
    return x % dimensionCount

def elapseOneSecond(grid: list[list[int]], 
                    botDict: dict[int, list[list[int, int], tuple[int, int]]]
                    ) -> None:
    rowNum = len(grid)
    colNum = len(grid[0])
    for i in range(len(botDict)):
        row, col = botDict[i][0]
        dx, dy = botDict[i][1]
        grid[row][col] -= 1
        newRow, newCol = correctGridValue(row + dx, rowNum), correctGridValue(col + dy, colNum)
        grid[newRow][newCol] += 1
        botDict[i][0] = (newRow, newCol)
        
def calcQuadrantBots(grid: list[list[int]], numRows: int, numCols: int):
    midRow = numRows // 2
    midCol = numCols // 2
    quadrantBots = [0, 0, 0,0]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i < midRow and j < midCol:
                quadrantBots[0] += grid[i][j]
            elif i < midRow and j > midCol:
                quadrantBots[1] += grid[i][j]
            elif i > midRow and j < midCol:
                quadrantBots[2] += grid[i][j]
            elif i > midRow and j > midCol:
                quadrantBots[3] += grid[i][j]
    return quadrantBots

def countMatchesAcrossAxis(grid: list[list[int]]):
    ct = 0
    for rowInd in range(len(grid)):
        newRow = grid[rowInd]
        l = 0
        r = len(newRow) - 1
        while l <=r:
            if grid[rowInd][l] > 0 and grid[rowInd][r] > 0:
                ct += 1
            l += 1
            r -= 1
    return ct

def countMatchesAcrossHorizontalAxis(grid: list[list[int]]):
    newGrid = []
    for col in range(len(grid[0])):
        newGridRow = []
        for row in range(len(grid)):
            newGridRow.append(grid[row][col])
        newGrid.append(newGridRow)
    return countMatchesAcrossAxis(newGrid)

def countSymmetricalRows(grid: list[list[int]]) -> bool:
    ct = 0
    for rowInd in range(len(grid)):
        newRow = [0 if i == 0 else 1 for i in grid[rowInd]]
        mid = len(newRow) // 2
        if newRow[:mid] == newRow[-1:mid:-1]:
            ct += 1
    return ct
        
def countSymmetricalCols(grid: list[list[int]]) -> bool:
    newGrid = []
    for col in range(len(grid[0])):
        newGridRow = []
        for row in range(len(grid)):
            newGridRow.append(grid[row][col])
        newGrid.append(newGridRow)
    return countSymmetricalRows(newGrid)

def calcSafetyFactor(quadrantBots: list[int]):
    prod = 1
    for i in range(len(quadrantBots)):
        prod *= quadrantBots[i]
    return prod

def getPrintable(grid: list[list[int]]):
    newGrid = []
    for row in range(len(grid)):
        newRow = []
        for col in range(len(grid[0])):
            val = grid[row][col] if grid[row][col] > 0 else "."
            newRow.append(val)
        newGrid.append(newRow)
    return newGrid

def getLongestConsecutiveLine(grid: list[list[int]]):
    maxLine = 0
    for row in range(len(grid)):
        # print(grid[row])
        longestLine = 0
        for col in range(len(grid[row])):
            if grid[row][col] >= 1:
                longestLine += 1
                maxLine = max(maxLine, longestLine)
            else:
                longestLine = 0
        longestLine = max(maxLine, longestLine)
    return longestLine
                    

if __name__ == '__main__':
    inputArray = getInput('./day14/input1.txt')
    NUM_COLS = 101
    NUM_ROWS = 103
    grid = initGrid(NUM_COLS, NUM_ROWS)
    botDict = initBotDict(inputArray)
    for i in range(len(botDict)):
        row, col = botDict[i][0]
        grid[row][col] += 1
    symmetryScores = []
    for i in range(100):
        elapseOneSecond(grid, botDict)
        quadrantBots = calcQuadrantBots(grid, NUM_ROWS, NUM_COLS)
        symmetryScores.append(abs(quadrantBots[0] - quadrantBots[1]) + abs(quadrantBots[2] - quadrantBots[3]))
    
    candidates = []
    for i in range(len(symmetryScores)):
        if symmetryScores[i] < 10:
            candidates.append(i)
    
    grid = initGrid(NUM_COLS, NUM_ROWS)
    botDict = initBotDict(inputArray)
    for i in range(len(botDict)):
        row, col = botDict[i][0]
        grid[row][col] += 1

    # print(countSymmetricalRows([[1, 0, 1],
    #                         [0, 1, 0],
    #                         [2, 0, 1],
    #                         [0, 2, 1]]))
    # print(countSymmetricalCols([  [1, 0, 1],
    #                         [0, 1, 0],
    #                         [2, 0, 1],
    #                         [0, 2, 1]]))
    # print(countMatchesAcrossAxis([[1, 0, 1],
    #                         [0, 1, 0],
    #                         [2, 0, 1],
    #                         [0, 2, 1]]))
    # print(countMatchesAcrossHorizontalAxis([[1, 0, 1],
    #                         [0, 1, 0],
    #                         [2, 0, 1],
    #                         [0, 2, 1]]))
    print(getLongestConsecutiveLine([[1, 0, 1],
                            [0, 1, 0],
                            [2, 0, 1],
                            [1, 2, 1, 1]]))
    for i in range(10000):
        elapseOneSecond(grid, botDict)
        quadrantBots = calcQuadrantBots(grid, NUM_ROWS, NUM_COLS)
        symmetryScore = abs(quadrantBots[0] - quadrantBots[1]) + abs(quadrantBots[2] - quadrantBots[3])
        # if symmetryScore == 0:
        #     print(' ========================')
        #     print(i)
        #     print(' ========================')
        #     print(countSymmetricalRows(grid))
            # symmetrical
        # symmetricalRows = countSymmetricalRows(grid)
        # symmetricalCols = countSymmetricalCols(grid)
        # matchesAcrossAxis = countMatchesAcrossAxis(grid)
        # matchesAcrossXAxis = countMatchesAcrossHorizontalAxis(grid)
        longestConsecutiveLine = getLongestConsecutiveLine(grid)
        if (longestConsecutiveLine > 15):
        # if (matchesAcrossAxis > 100 or (matchesAcrossXAxis > 100)):
            # print(f"Iteration {i}, has symmetrical rows: {symmetricalRows}, symmetrical columns: {symmetricalCols}, matches across axis: {matchesAcrossAxis}, matches across x axis: {matchesAcrossXAxis}")
            print(f"At iteration {i}, longest conecutive line was {longestConsecutiveLine}")
            # print(i)
            
            printableGrid = getPrintable(grid)
            print()

            with open(f"output{i}.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(printableGrid)