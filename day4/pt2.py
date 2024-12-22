def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]


def searchForXmasInDirection(grid: list[str], dir: tuple[int, int], x: int, y: int) -> bool:
    if grid[x][y] != 'A':
        return False
    x, y = x + dir[0], y + dir[1]
    dir = dir[0] * -1, dir[1] * -1
    
    if grid[x][y] == 'S':
        searchTerm = 'SAM'
    else:
        searchTerm = 'MAS'
    for i in range(3):
        if ((not (0 <= x < len(grid))) 
            or (not (0 <= y < len(grid[0])))
            or grid[x][y] != searchTerm[i]):
            return False
        x += dir[0]
        y += dir[1]
    return True

def countXmas(grid: list[str]):
    dirs = [(-1, -1), (-1, 1)]
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += (searchForXmasInDirection(grid, dirs[0], i, j) and searchForXmasInDirection(grid, dirs[1], i, j))
    return total
                

if __name__ == '__main__':
    grid = getInput('./day4/input0.txt')
    print(countXmas(grid))
    # print(grid)
