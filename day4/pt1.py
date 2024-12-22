def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]


def searchForXmasInDirection(grid: list[str], dir: tuple[int, int], x: int, y: int) -> bool:
    searchTerm = 'XMAS'
    for i in range(4):
        if ((not (0 <= x < len(grid))) 
            or (not (0 <= y < len(grid[0])))
            or grid[x][y] != searchTerm[i]):
            return False
        x += dir[0]
        y += dir[1]
    return True

def countXmas(grid: list[str]):
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dir in dirs:
                total += searchForXmasInDirection(grid, dir, i, j)
    return total
                
                    
        
        
    
    
    

if __name__ == '__main__':
    grid = getInput('./day4/input1.txt')
    print(countXmas(grid))
    # print(grid)
