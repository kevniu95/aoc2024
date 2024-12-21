import heapq

def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def processInput(inputArray: list[str]) -> tuple[list[list[int]], list[int]]:
    grid = []
    for line in inputArray:
        line = line.strip()
        if len(line) > 0:
            if line.startswith('#'):
                grid.append([i for i in line])
    return grid



dirMap = {'>': (0, 1),
          'v': (1, 0),
          '<': (0, -1),
          '^' : (-1, 0)}

def bfsTraversal(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    x, y = start[0], start[1]
    for dir, dirVal in dirMap.items():
        newx, newy = x + dirVal[0], y + dirVal[1]
        print(newx, newy)
        

if __name__ == '__main__':
    inputArray = getInput('./day16/input0.txt')
    grid = processInput(inputArray)
    
    orientation = '>'

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'E':
                end = row, col
            if grid[row][col] == 'S':
                start = row, col
    bfsTraversal(grid, start, end)
    # print(start)
    # print(end)

    # grid, instructions = processInput(inputArray)
    # robotPos = getInitRobotPosition(grid)

    # for instruction in instructions:
    #     robotPos = moveBot(instruction, grid, robotPos)
    # print(calcGpsSum(grid))

