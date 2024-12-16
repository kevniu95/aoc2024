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
        
    def inbounds(self, arr: list[list[int]], x: int, y: int) -> bool:
        return 0 <= x < len(inputArray) and 0 <= y < len(inputArray[0])

    # def visit(self, 
    #           inputArray: list[list[int]], 
    #           x: int, 
    #           y: int, 
    #           entries = 0, 
    #           borders = 0) -> int:
    #     letter = inputArray[x][y]
    #     for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    #         x1, y1 = x + i[0], y + i[1]
    #         if self.inbounds(inputArray, x1, y1) and (x1, y1) not in self.seenSet and inputArray[x1][y1] == letter:
                  
    def visit(self, x: int, y: int, grid: list[list[int]], ovrSet: set[int], roundSet: set[int]) -> int:
        sides = 0
        for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            curr_x, curr_y = x + i[0], y + i[1]
            # print(curr_x, curr_y)
            # print(grid)
            if 0 <= curr_x < len(grid) and 0 <= curr_y < len(grid[0]) and grid[curr_x][curr_y] == grid[x][y]:
                id = (curr_x, curr_y)
                ovrSet.add(id)
                if id not in roundSet:
                    sides += 1
        return sides
                    
        
    def getShape(self, x: int, y: int, grid: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
        q = deque()
        q.append((x, y))
        ovrSet = set()
        ovrSet.add((x, y))
        sides = 0
        letter = grid[x][y]
        round = 0
        while q:
            # print(f"Round {round}")
            roundSet = ovrSet.copy()
            while q:
                curr_x, curr_y = q.popleft()
                sides += self.visit(curr_x, curr_y, grid, ovrSet, roundSet)
            q = deque(list(ovrSet.difference(roundSet)))
            # print(sides)
            # print(q)
            round += 1
            # print()
        return sides, ovrSet

    def process(self, grid: list[list[int]]) -> int:
        ansArr = []
        overallSet = set()
        total = 0
        for x in range(len(grid)):
            for y in range(len(inputArray[0])):
                if (x, y) not in overallSet:
                    print(grid[x][y])
                    sides, bfsSet = self.getShape(x, y, grid)
                    ansArr.append((sides, len(bfsSet)))
                    overallSet.update(bfsSet)
                    print(ansArr)
        for ans in ansArr:
            neighboring_sides, count = ans[0], ans[1]
            perimeter = count * 4 - 2 * neighboring_sides
            print(f"count was {count}, perimeter was {perimeter}, ")
            print(f"Product of the two was {perimeter * count}")
            total += count * perimeter
            
        return total

    



    # def process(self, inputArray: list[list[int]]):
    #     # Idea: BFS search from each letter if not in seen set
    #     # Regions can repeat letters
    #     seenSet = set()
    #     for x in len(inputArray):
    #         for y in len(inputArray[0]):
    #             if inputArray[x][y] not in seenSet:
    #                 self.visit(inputArray, x, y, )
                    
    #             letter = inputArray[x][y]
    #             for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    #                 x1, y1 = x + i[0], y + i[1]
    #                 if self.inbounds(inputArray, x1, y1) and (x1, y1) not in self.seenSet and inputArray[x1][y1] == letter:
                
    #             if (x, y) not in seenSet:
    #                 visit(x, y)
        

if __name__ == '__main__':
    inputArray = getInput('./day12/input2.txt')
    inputArray = processInput(inputArray)
    a = Solution()
    print(a.process(inputArray))