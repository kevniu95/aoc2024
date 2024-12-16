def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def processInput(inputArray: list[str]) -> tuple[list[list[int]], list[int]]:
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

def moveBot(instr: str, grid: list[list[str]], robotPos: list[int, int]) -> list[int, int]:
    dir = DIR_DICT[instr]
    x, y = robotPos
    newx, newy = x + dir[0], y + dir[1]
    if grid[newx][newy] == '#':
        return robotPos
    elif grid[newx][newy] == '.':
        grid[x][y] = '.'
        grid[newx][newy] = '@'
        return [newx, newy]
    elif grid[newx][newy] == 'O':
        endOfBoxes = getBoxShiftPosition(newx, newy, dir, grid)
        if endOfBoxes:
            grid[x][y] = '.'
            grid[endOfBoxes[0]][endOfBoxes[1]] = 'O'
            grid[newx][newy] = '@'
            return [newx, newy]
    return [x, y]
        
def calcGpsSum(grid: list[list[int]]):
    gpsSum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                gpsSum += i * 100 + j
    return gpsSum

if __name__ == '__main__':
    inputArray = getInput('./day15/input2.txt')
    grid, instructions = processInput(inputArray)
    robotPos = getInitRobotPosition(grid)

    for instruction in instructions:
        robotPos = moveBot(instruction, grid, robotPos)
    print(calcGpsSum(grid))

