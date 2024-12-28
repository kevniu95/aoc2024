from collections import defaultdict
import time

def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()    
    return data


def processInput(data: list[str]) -> list[list[str]]:
    grid = []
    for line in data:
        grid.append([i for i in line.strip()])
    return grid


def getStart(grid: list[list[str]]):
    start, end = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'E':
                end = (i, j)
    return start, end

def walkPath(grid: list[list[str]],
             start: tuple[int, int], 
             end: tuple[int, int],
             path_cells: list[tuple[int, int]],
             cell_dict: dict[tuple[int, int], int]
             ) -> None:
    curr = start
    path_cells.append(curr)
    cell_dict[start] = 0
    while curr != end:
        for i in [(-1, 0),
                  (1, 0),
                  (0, 1),
                  (0, -1)]:
            x, y = curr[0] + i[0], curr[1] + i[1]
            i2 = tuple(j * 2 for j in i)
            x2, y2 = curr[0] + i2[0], curr[1] + i2[1]
            if (x, y) not in cell_dict and 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#':
                curr_d = cell_dict[curr]
                path_cells.append((x, y))
                cell_dict[(x, y)] = curr_d + 1
                curr = (x, y)
                
    return


def countCheats(path_cells: list[tuple[int, int]], cell_dict: dict[tuple[int, int]]):
    ct = 0
    for i in range(len(path_cells)):
        for j in range(i + 1, len(path_cells)):
            cell1 = path_cells[i] 
            cell2 = path_cells[j]

            dist1 = cell_dict[cell1]
            dist2 = cell_dict[cell2]

            minDistanceBetweenCells = abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])
            if 100 <= dist2 - dist1 - minDistanceBetweenCells and minDistanceBetweenCells <= 20:
                ct += 1
    return ct
    

if __name__ == '__main__':
    data = getInput('./day20/input1.txt')
    grid = processInput(data)

    start, end = getStart(grid)
    print(start, end)

    path_cells: list[tuple[int, int]] = []
    cell_dict: dict[tuple[int, int], int] = {}
    cheat_dict: dict[tuple[int, int], int] = defaultdict(list)
        
    walkPath(grid, start, end, path_cells, cell_dict)

    print(countCheats(path_cells, cell_dict))