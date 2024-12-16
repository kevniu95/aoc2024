def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def doDoubleGrid(grid: list[list[int]]) -> list[list[int]]:
    doubleDict= {
        '#': '##',
        '.' : '..',
        'O' : '[]',
        '@' : '@.'
    }
    newGrid = []
    for row in grid:
        newRow = []
        for j in range(len(row)):
            newRow.append(doubleDict[row[j]])
        newRow = [i for i in ''.join(newRow)]
        newGrid.append(newRow)
    return newGrid
    

def processInput(inputArray: list[str], doubleGrid: bool = True) -> tuple[list[list[int]], list[int]]:
    grid = []
    instructions = []
    for line in inputArray:
        line = line.strip()
        if len(line) > 0:
            if line.startswith('#'):
                grid.append([i for i in line])
            elif not line.startswith('##'):
                instructions.append(line)
    instructions = ''.join(instructions)
    if doubleGrid:
        grid = doDoubleGrid(grid)
    return grid, instructions

def getInitRobotPosition(grid) -> list[int, int]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                return [row, col]

DIR_DICT= {
        '<' : [0, -1],
        '^' : [-1, 0],
        '>' : [0, 1],
        'v' : [1, 0],
    }
     
def getBoxShiftPosition(x: int, y: int, dir: tuple[int, int], grid: list[list[int]]) -> tuple[int, int]:
    """
    If boxes can be shifted, returns new position of last box in line
      - Then we can simply move first box in line to last box of line
      - And put robot where first box of line is
      - Save some operations
    """
    while grid[x][y] == 'O':
        x, y = x + dir[0], y + dir[1]
    if grid[x][y] == '#':
        return
    elif grid[x][y] == '.':
        return x, y

def canHorizontalPush(x: int, 
                      y: int,
                      dir: tuple[int, int], 
                      grid: list[list[int]]) -> bool:
    # Horizontal push
    while grid[x][y] in ['[', ']']:
        x, y = x + dir[0], y+ dir[1]
    if grid[x][y] == '#':
        return False
    elif grid[x][y] == '.':
        return True
  
def doHorizontalPush(x: int,
                     y: int,
                     dir: tuple[int, int],
                     grid: list[list[int]]
                     )->  None:
    '''
    Slides boxes down horizontal direction
    Track lastVal seen, so we can put it in new cell. 
    On first iteration, lastVal is robot moving into cell previously containing box
    '''
    # We are sliding values down, the first time, we slide robot into first seen box position
    lastVal = '@' 
    while lastVal in ['[', ']', '@']:
        val = grid[x][y]
        grid[x][y] = lastVal
        x, y = x + dir[0], y+ dir[1]
        lastVal = val

def canVerticalPush(x: int,
                    y: int,
                    dir: tuple[int, int],
                    grid: list[list[int]]) -> bool:
    # Idea
    # Recursively-defined vertical push function?
    if grid[x][y] == '#':
        return False
    elif grid[x][y] == '.':
        return True
    else:
        if grid[x][y] == '[':
            neighbor_x, neighbor_y = x, y + 1            
        elif grid[x][y] == ']':
            neighbor_x, neighbor_y = x, y - 1
        
        x1, y1 = x + dir[0], y + dir[1]
        x2, y2 = neighbor_x + dir[0], neighbor_y + dir[1]
        
        return canVerticalPush(x1, y1, dir, grid) and canVerticalPush(x2, y2, dir, grid)

# def doVerticalPush(x: int,
#                     y: int,
#                     dir: tuple[int, int],
#                     grid: list[list[int]],
#                     lastValue: str) -> None:
#     if (x, y) in VERTICAL_PUSHED_SET:
#         return
#     # print(f"Called do vertical push on {x}, {y}")
#     thisValue = grid[x][y]
#     # print(thisValue)
#     if thisValue == '[':
#         neighborValue = ']'
#         neighbor_x, neighbor_y = x, y + 1            
#     elif thisValue == ']':
#         neighborValue = '['
#         neighbor_x, neighbor_y = x, y - 1
#     if thisValue in ['[', ']']:
#         x1, y1 = x + dir[0], y + dir[1]
#         x2, y2 = neighbor_x + dir[0], neighbor_y + dir[1]
#         doVerticalPush(x1, y1, dir, grid, thisValue)
#         doVerticalPush(x2, y2, dir, grid, neighborValue)
#     grid[x][y] = lastValue
#     VERTICAL_PUSHED_SET.add((x, y))
#     return 

def canPush(newx, newy, dir, grid) -> bool:
    x, y = newx, newy
    if abs(dir[1]) == 1:
        return canHorizontalPush(x, y, dir, grid)
    else:
        canVerticalPushResult = canVerticalPush(x, y, dir, grid)
        print(f"Canvertpushresult: {canVerticalPushResult}")
        return canVerticalPushResult

def doVerticalPush(x: int, y: int, dir: tuple[int, int], grid: list[list[int]]):
    '''
    p stands for pushee (or cell being pushed)
    '''
    myValue = grid[x][y]
    p1_x, p1_y = x + dir[0], y + dir[1]
    if grid[p1_x][p1_y] == '.':
        grid[p1_x][p1_y] = myValue
        grid[x][y] = '.'
        return
    if grid[p1_x][p1_y] == '[':
        p2_x, p2_y = x + dir[0], y + dir[1] + 1
    else:
        p2_x, p2_y = x + dir[0], y + dir[1] - 1
    doVerticalPush(p1_x, p1_y, dir, grid)
    doVerticalPush(p2_x, p2_y, dir, grid)
    grid[p1_x][p1_y] = myValue
    if myValue == '@':
        grid[p2_x][p2_y] = "."
    grid[x][y] = '.'

def doPush(x, y, newx, newy, dir, grid) -> bool:
    if abs(dir[1]) == 1:
        doHorizontalPush(newx, newy, dir, grid)
        grid[x][y] = '.'
    else:
        doVerticalPush(x, y, dir, grid)

        
def moveBot(instr: str, grid: list[list[str]], robotPos: list[int, int]) -> list[int, int]:
    dir = DIR_DICT[instr]
    x, y = robotPos
    print(f"Robot is at {x}, {y}")
    newx, newy = x + dir[0], y + dir[1]
    if grid[newx][newy] == '#':
        return robotPos
    elif grid[newx][newy] == '.':
        grid[x][y] = '.'
        grid[newx][newy] = '@'
        return [newx, newy]
    elif grid[newx][newy] in ['[', ']']:
        # Check if can push
        if canPush(newx, newy, dir, grid):
            doPush(x, y, newx, newy, dir, grid)
            return [newx, newy]
    return [x, y]
        
def calcGpsSum(grid: list[list[int]]):
    gpsSum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '[':
                gpsSum += i * 100 + j
    return gpsSum

if __name__ == '__main__':
    inputArray = getInput('./day15/input2.txt')
    grid, instructions = processInput(inputArray)
    robotPos = getInitRobotPosition(grid)
    [print(line) for line in grid]
    # print(instructions)
    ind = 0
    print(len(instructions))
    for instruction in instructions:
        # print(f"Here is instruction index {ind}: {instruction}")
        robotPos = moveBot(instruction, grid, robotPos)
        # [print(line) for line in grid]
        # print(instructions)
        # print()
        ind += 1
    [print(line) for line in grid]
    # print(instructions)
    # print()
        
    print(calcGpsSum(grid))

