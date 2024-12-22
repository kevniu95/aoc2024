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

def findStartEnd(grid: list[str]) -> tuple[list[int, int], list[int, int]]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'E':
                end = row, col
            if grid[row][col] == 'S':
                start = row, col
    return start, end
    
dirMap = {'>': (0, 1),
          'v': (1, 0),
          '<': (0, -1),
          '^' : (-1, 0)}

# def bfsTraversal(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
#     x, y = start[0], start[1]
#     for dir, dirVal in dirMap.items():
#         newx, newy = x + dirVal[0], y + dirVal[1]
#         if grid[newx][newy] == '#' or :
#             continue
#         elif grid[]

# class 

def shortestPath(grid, start, end):
    s = [5, start[0], start[1]] # try with d, x, y, and d first to see if it works w/ heapify?
    q = []
    heapq.heappush(q, s)
    while q:
        curr = heapq.heappop(q)
        x, y = curr[1], curr[2]
        for i, j in [(0,1),(0,-1),(-1,0),(1,0)]:
            x1, y1 = x + i , y + j

        
            
        

    

if __name__ == '__main__':
    inputArray = getInput('./day16/input0.txt')
    grid = processInput(inputArray)
    
    orientation = '>'

    [print(row) for row in grid]

    start, end = findStartEnd(grid)

    print(start, end)

    shortestPath(grid, start, end)

    # for row in range(len(grid)):
    #     for col in range(len(grid[0])):
    #         if grid[row][col] == 'E':
    #             end = row, col
    #         if grid[row][col] == 'S':
    #             start = row, col
    # bfsTraversal(grid, start, end)
    # print(start)
    # print(end)

    # grid, instructions = processInput(inputArray)
    # robotPos = getInitRobotPosition(grid)

    # for instruction in instructions:
    #     robotPos = moveBot(instruction, grid, robotPos)
    # print(calcGpsSum(grid))

