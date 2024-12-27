from collections import defaultdict

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

def evaluateCheats(grid: list[list[str]],
             start: tuple[int, int], 
             end: tuple[int, int],
             path_cells: list[tuple[int, int]],
             cell_dict: dict[tuple[int, int]],
             cheat_dict: dict[tuple[int, int], list[int]]
             ) -> None:
    curr = start
    for curr in path_cells:
        for i in [(-1, 0),
                  (1, 0),
                  (0, 1),
                  (0, -1)]:
            x, y = curr[0] + i[0], curr[1] + i[1]
            i2 = tuple(j * 2 for j in i)
            x2, y2 = curr[0] + i2[0], curr[1] + i2[1]
            if grid[x][y] == '#' and 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and (x2, y2) in cell_dict:
                cheatGain = -(cell_dict[curr] - cell_dict[(x2, y2)]) - 2
                if cheatGain > 0:
                    cheat_dict[curr].append(cheatGain)
                
    return cheat_dict


if __name__ == '__main__':
    data = getInput('./day20/input1.txt')
    grid = processInput(data)

    start, end = getStart(grid)
    print(start, end)

    path_cells: list[tuple[int, int]] = []
    cell_dict: dict[tuple[int, int], int] = {}
    cheat_dict: dict[tuple[int, int], int] = defaultdict(list)
    
    
    walkPath(grid, start, end, path_cells, cell_dict)

    # print(path_cells)
    # print()
    # print(cell_dict)

    cheat_dict = evaluateCheats(grid, start, end, path_cells, cell_dict, cheat_dict)
    
    # print(cheat_dict)

    finalList = []
    for k, v in cheat_dict.items():
        finalList.extend([i for i in v if i >= 100])
    print(len(finalList))