from collections import defaultdict
def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def getGrid(inputArray: list[str]) -> list[list[str]]:
    outlines = []
    for line in inputArray:
        outline = []
        for chr in line.strip():
            outline.append(chr)
        outlines.append(outline)
    return outlines

def getCommonLetters(grid: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    frequencies: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            letter = grid[i][j]
            if letter != '.':
                frequencies[letter].append((i, j))
    return frequencies


def getAntinode(node1: tuple[int, int],
                node2: tuple[int, int]) -> tuple[int, int]:
    x_diff = node1[0] - node2[0]
    y_diff = node1[1] - node2[1]

    x1 = node1[0] + x_diff
    y1 = node1[1] + y_diff
    return x1, y1
    

def inGrid(node: tuple[int, int], grid: list[list[str]]) -> bool:
    return (0 <= node[0] < len(grid) 
            and 0 <= node[1] < len(grid[0]))
    

def addNodes(startNode: tuple[int, int], 
             s_x: int, 
             s_y: int,
             mul: int,
             grid: list[list[str]],
             allAntinodes: set[tuple[int, int]]) -> None:
    x, y = startNode[0], startNode[1]
    while inGrid((x, y), grid):
        allAntinodes.add((x, y))
        x += (mul * s_x)
        y += (mul * s_y)
        

def addAntinodesForLetter(locations: list[tuple[int, int]], 
                            grid: list[list[str]],
                            allAntinodes: set[tuple[int, int]]):
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            s_x = locations[i][0] - locations[j][0]
            s_y = locations[i][1] - locations[j][1]
            addNodes(locations[i], s_x, s_y, -1, grid,allAntinodes)
            addNodes(locations[i], s_x, s_y, 1, grid,allAntinodes)
    # print(allAntinodes)
    return len(allAntinodes)


if __name__ == '__main__':
    inputArray = getInput('./day8/input3.txt')
    # print(inputArray)
    grid = getGrid(inputArray)
    commonLetters = getCommonLetters(grid)
    print(commonLetters)
    print(len(grid))
    print(len(grid[0]))
    
    allAntinodes = set()
    for k, v in commonLetters.items():
        print(addAntinodesForLetter(v, grid, allAntinodes))
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if ((i, j) in allAntinodes) and grid[i][j]=='.':
                grid[i][j] = '#'
    
    # [print(line) for line in grid]
        
        