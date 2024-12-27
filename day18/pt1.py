
from collections import deque

def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    
    return [i.strip() for i in data]


def initGrid():
    lines = []
    for i in range(DIMS):
        line = []
        for j in range(DIMS):
            line.append('.')
        lines.append(line)
    return lines
    

def placeBytes(byts: tuple[int, int], numBytes: int, grid: list[list[str]]):
    for byt in byts[:numBytes + 1]:
        x, y = byt.split(',')
        x, y = int(x), int(y)
        grid[y][x] = '#'
        # grid[byt[0]][byt[1]] = '#'
    return grid
               

def getToEnd(grid: list[list[int]]):
    s = (0, 0)
    q = deque()
    q.append(s)
    final = {s: 0}
    while q:
        curr_x, curr_y = q.popleft()
        d = final[(curr_x, curr_y)]
        for i in [(0, -1),
                    (0, 1),
                    (1, 0),
                    (-1, 0)]:
            x, y  = curr_x + i[0], curr_y + i[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#' and (x, y) not in final:
                final[(x, y)] = d + 1
                q.append((x, y))
            if (x, y) == ((DIMS - 1), (DIMS - 1)):
                return d + 1  
    return


if __name__ == '__main__':
    byts = getInput('./day18/input1.txt')
    DIMS = 71


    # =========
    # Pt 1
    # =========
    grid = initGrid()
    placeBytes(byts, 1024, grid)
    print(getToEnd(grid))

    # =========
    # Pt 2
    # =========
    for i in range(1024, 4900):
        print(f"Bytes placed: {i}")
        grid = initGrid()
        grid = placeBytes(byts, i, grid)
        ans = getToEnd(grid)
        if not ans:
            print(i)
            print(f"Last placed coordinate: {byts[i]}")
            break
        