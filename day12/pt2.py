from collections import deque
def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def processInput(str_input: str) -> list[list[str]]:
    ovr_arr = []
    for line in str_input:
        line = line.strip()
        curr_arr = []
        for letter in line:
            curr_arr.append(letter)
        ovr_arr.append(curr_arr)
    return ovr_arr
  

class Solution:
    def __init__(self):
        self.seenSet = set()
        self.ct = 0
        
    def visit(self, x: int, y: int, grid: list[list[int]], ovrSet: set[int], roundSet: set[int]) -> int:
        for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            curr_x, curr_y = x + i[0], y + i[1]
            if 0 <= curr_x < len(grid) and 0 <= curr_y < len(grid[0]) and grid[curr_x][curr_y] == grid[x][y]:
                ovrSet.add((curr_x, curr_y))
                    
    def getShape(self, x: int, y: int, grid: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
        q = deque([(x,y)])
        ovrSet = set([(x, y)])
        while q:
            roundSet = ovrSet.copy()
            while q:
                curr_x, curr_y = q.popleft()
                self.visit(curr_x, curr_y, grid, ovrSet, roundSet)
            q = deque(list(ovrSet.difference(roundSet)))
        return ovrSet

    def initBFS(self, grid: list[list[int]]) -> int:
        overallSet = set()
        shapeAreas = []
        squareToShapeMapper = {}
        for x in range(len(grid)):
            for y in range(len(inputArray[0])):
                if (x, y) not in overallSet:
                    bfsSet = self.getShape(x, y, grid)
                    shapeAreas.append(len(bfsSet))
                    for i in bfsSet:
                        squareToShapeMapper[i] = len(shapeAreas) - 1
                    overallSet.update(bfsSet)
        return shapeAreas, squareToShapeMapper

    
    def doDirectionalDfsVisit(self,
                              x: int,
                              y: int,
                              grid: list[list[int]],
                              dir: tuple[int, int],
                              dirSet: set[tuple[int, int]]
                              )-> bool:
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return
        self.ct += 1
        new_x, new_y = x + dir[0], y+ dir[1]
        if ((0 <= new_x < len(grid) 
                and 0 <= new_y < len(grid[0]) 
                and grid[new_x][new_y] == grid[x][y])
            or 
              (x, y) in dirSet
            or (new_x < -1 or new_y < -1)):
            return False
        else:    
            dirSet.add((x, y))
            if abs(dir[0]) == 1:
                if 0 <= x < len(grid) and 0 <= y  - 1< len(grid[0]) and grid[x][y] == grid[x][y - 1]:
                    self.doDirectionalDfsVisit(x, y - 1, grid, dir, dirSet)
                if 0 <= x < len(grid) and 0 <= y  + 1< len(grid[0]) and grid[x][y] == grid[x][y + 1]:
                    self.doDirectionalDfsVisit(x, y + 1, grid, dir, dirSet)
            else:
                if 0 <= x + 1 < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == grid[x + 1][y]:
                    self.doDirectionalDfsVisit(x + 1, y, grid, dir, dirSet)
                if 0 <= x - 1 < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == grid[x - 1][y]:
                    self.doDirectionalDfsVisit(x - 1, y, grid, dir, dirSet)
            return True
        
    
    
    def doDirectionalDfs(self,
                         grid: list[list[int]], 
                         dir: tuple[int, int], 
                         shapeSides: dict[int, int], 
                         cellToShapeMapper: dict[tuple[int, int], int]):
        dirSet = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if self.doDirectionalDfsVisit(x, y, grid, dir, dirSet):
                    updateShape = cellToShapeMapper[(x, y)]
                    shapeSides[updateShape] = shapeSides.get(updateShape, 0) + 1
        return
        
    
    def returnShapeSides(self, 
                         grid: list[list[int]], 
                         cellToShapeMapper: dict[tuple[int, int], int]) -> dict[int, int]:
        shapeSides= {}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dir in dirs:
            self.doDirectionalDfs(grid, dir, shapeSides, cellToShapeMapper)
        return shapeSides

if __name__ == '__main__':
    inputArray = getInput('./day12/input2.txt')
    inputArray = processInput(inputArray)
    a = Solution()
    shapeAreas, squareToShapeMapper = a.initBFS(inputArray)
    
    shapeSides = a.returnShapeSides(inputArray, squareToShapeMapper)

    out = []
    for i in range(len(shapeAreas)):
        out.append(shapeAreas[i]*shapeSides[i])
    print(out)
    print(sum(out))