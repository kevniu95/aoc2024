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
    def __init__(self, x: int, y: int, d: int, o: str, p = None):
        """
        Where 'o' stands for orientation
        """
        self.x = x
        self.y = y
        self.d = d       
        self.o = o
        self.p = None

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
        return f"Cell at {self.x}, {self.y} with distance {self.d}"
    
    def __repr__(self) -> str:
        return f"Cell at {self.x}, {self.y} with distance {self.d}"
    

def upsertCell(x: int,
               y: int,
               px: int,
               py: int,
               d: int,
               o: str,
               cellDict: dict[tuple[int, int], ShortestPathGridCell], 
               q: list[ShortestPathGridCell],
               finished: set[ShortestPathGridCell]) -> None:
    """
    Add cell to cell dict and q
    If already exists, update d
    """
    cell = cellDict.get((x, y), None)
    if cell and d < cell.d:
        cell = cellDict[(x, y)]
        cell.d = d
        cell.o= o
        if px and py:
            cell.p = cellDict.get((px, py,), None)
    elif not cell:
        cell = ShortestPathGridCell(x, y, d, o)
        cellDict[(x, y)] = cell
        if px and py:
            cell.p = cellDict.get((px, py,), None)
    if (cell.x, cell.y) not in finished:
        heapq.heappush(q, cell)        

ORIENTATION_MAP = {'>': (0, 1),
          'v': (1, 0),
          '<': (0, -1),
          '^' : (-1, 0)}

ORIENTATION_MAP_FLIPPED = {v:k for k,v in ORIENTATION_MAP.items()}

def calcDistanceToNeighbor(orientation: tuple[int, int], cellDir: tuple[int, int], curr_d) -> int:
    o = ORIENTATION_MAP[orientation]
    if o == cellDir:
        return 1 + curr_d
    elif ((o[0] + cellDir[0]) * (o[1] + cellDir[1])) == 0: 
        return 2001 + curr_d
    else:
        return 1001 + curr_d
    

def shortestPath(grid, start, end):
    o = '>'
    cellDict = {}
    q = []
    finished = set()
    upsertCell(start[0], start[1], None, None, 0, o, cellDict, q, finished)
    ind = 0
    while q:
        currCell = heapq.heappop(q)
        if (end[0], end[1]) == (currCell.x, currCell.y):
            # print("I am ending this")
            # print(currCell)
            break
        finished.add((currCell.x, currCell.y))
        # print(f"Adding {currCell.x}, {currCell.y} at distance {currCell.d}")
        # print(f"Current orientation is {o}")
        o = currCell.o
        x, y = currCell.x, currCell.y
        for i, j in [(0,1),(0,-1),(-1,0),(1,0)]:
            x1, y1 = x + i , y + j
            if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
                if grid[x1][y1] == '#':
                    upsertCell(x1, y1, x, y, math.inf, o, cellDict, q, finished)
                else:
                    if grid[x1][y1] in ['.', 'E']:
                        curr_d = currCell.d
                        d = calcDistanceToNeighbor(o, (i, j), curr_d)
                        upsertCell(x1, y1, x, y, d, ORIENTATION_MAP_FLIPPED[(i, j)], cellDict, q, finished)
        ind += 1
            
    return cellDict[(end[0], end[1])],cellDict, finished
        
if __name__ == '__main__':
    inputArray = getInput('./day16/input1.txt')
    grid = processInput(inputArray)
    
    orientation = '>'

    # [print(row) for row in grid]
    start, end = findStartEnd(grid)
    finalCell, cellDict, finished = shortestPath(grid, start, end)
    
    currCell = finalCell
    ct = 1
    while currCell:
        currCell = currCell.p
        ct += 1
        # cellDict.get((p.x, p.y))
        # print(cellDict.get((currCell.x, currCell.y)))
        # print(p)
        # ct += 1
    print(ct)
        
    # for f in finished:
    #     print(cellDict[f])