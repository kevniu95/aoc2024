import heapq
import math

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
    
class ShortestPathGridCell():
    def __init__(self, x: int, y: int, o: str, d: int):
        """
        Where 'o' stands for orientation

        For pt2, conceive of x,y,o as marker of a distinct cell (instead of just x, y)
        """
        self.x = x
        self.y = y
        self.o = o
        self.d = d       
        self.p = []

    def __eq__(self, other):
        if isinstance(other, ShortestPathGridCell):
            return self.d == other.d
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, ShortestPathGridCell):
            return self.d <= other.d
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, ShortestPathGridCell):
            return self.d < other.d
        return NotImplemented

    def __str__(self) -> str:
        return f"Cell at {self.x}, {self.y}, {self.o} with distance {self.d}"
    
    def __repr__(self) -> str:
        return f"Cell at {self.x}, {self.y}, {self.o} with distance {self.d}"
           

ORIENTATION_MAP = {'>': (0, 1),
          'v': (1, 0),
          '<': (0, -1),
          '^' : (-1, 0)}

ORIENTATION_MAP_FLIPPED = {v:k for k,v in ORIENTATION_MAP.items()}

def findCellInDirection(currCell: ShortestPathGridCell, 
                        o: str, 
                        grid: list[list[str]],
                        cellDict: dict[tuple[int, int, str], ShortestPathGridCell],
                        q: list[ShortestPathGridCell]) -> ShortestPathGridCell:
    """
    Returns neighboring cell to cell being taken off queue
    Where o is orientation being considered for traversal
    Compare this to currCell.o
    """
    x, y = currCell.x, currCell.y
    if o == currCell.o:
        x += ORIENTATION_MAP[o][0]
        y += ORIENTATION_MAP[o][1]
    
    if not( 0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == '#':
        return None
    
    returnCell = cellDict.get((x, y, o), ShortestPathGridCell(x, y, o, math.inf))
    if (x, y, o) not in cellDict:
        cellDict[(x, y, o)] = returnCell    
    return returnCell

def getNeighborDistance(currCell: ShortestPathGridCell, neighborCell: ShortestPathGridCell) -> int:
    if currCell.o == neighborCell.o:
        return 1
    c_x, c_y = ORIENTATION_MAP[currCell.o]
    n_x, n_y = ORIENTATION_MAP[neighborCell.o]
    if (c_x + n_x) * (c_y + n_y) == 0: 
        return 2000
    return 1000


def updateNeighbor(currCell: ShortestPathGridCell, 
                   neighborCell: ShortestPathGridCell,
                   d: int,
                   q: list[ShortestPathGridCell]) -> None:
    if currCell.d + d < neighborCell.d:
        neighborCell.d = currCell.d + d
        neighborCell.p = [currCell]
        heapq.heappush(q, neighborCell)
    elif currCell.d + d == neighborCell.d:
        neighborCell.p.append(currCell)
        

def shortestPath(grid, start, end):
    cellDict = {}
    q = []
    startCell = ShortestPathGridCell(start[0], start[1], '>', 0)
    cellDict[(start[0], start[1], '>')] = startCell
    q.append(startCell)
    finished = set()
    while q:
        currCell = heapq.heappop(q)
        if (currCell.x, currCell.y) == (end[0], end[1]):
            break
        finished.add((currCell.x, currCell.y))
        for o, o_num in ORIENTATION_MAP.items():
            neighborCell = findCellInDirection(currCell, o, grid, cellDict, q)
            if neighborCell:
                distance = getNeighborDistance(currCell, neighborCell)
                updateNeighbor(currCell, neighborCell, distance, q)
        
    answerDict = {}
    for i in ['^', 'v', '>', '<']:
        answerDict[i] = cellDict.get((end[0], end[1], i), None)
    return answerDict
        
        
if __name__ == '__main__':
    inputArray = getInput('./day16/input2.txt')
    grid = processInput(inputArray)
    
    orientation = '>'

    # [print(row) for row in grid]
    start, end = findStartEnd(grid)
    answerDict = shortestPath(grid, start, end)

    finalCell = answerDict['>'] 
    # Just looked at answer for input to confirm one path
    processCells = [finalCell]
    answerSet = set([])
    while len(processCells) > 0:
        currCell = processCells.pop(0)
        processCells.extend(currCell.p)
        if (currCell.x, currCell.y) not in answerSet:
            answerSet.add((currCell.x, currCell.y))
        
