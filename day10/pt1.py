def getInputArray(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    out = []
    for line in data:
        out.append([int(j) if '0' <= j <= '9' else j for j in line.strip()])
    return out

def getStarts(inputArray: list[list[int]]):
    heads = []
    for i in range(len(inputArray)):
        for j in range(len(inputArray[i])):
            if inputArray[i][j] == 0:
                heads.append((i, j))
    return heads
    

def getScore(inputArray: list[list[int]], 
             x: int, 
             y: int
             ) -> int:
    endSets = set()
    # rating = 0 
    def recursiveGetScore(inputArray: list[list[int]], 
                x: int, 
                y: int,
                endSets: set[tuple[int, int]],
                ) -> int:
        if inputArray[x][y] == 9:
            # rating += 1
            endSets.add((x, y))
        for a, b in [(-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)]:
            new_x = x + a
            new_y = y + b
            if 0 <= new_x < len(inputArray) and 0 <= new_y < len(inputArray[0]):
                if inputArray[new_x][new_y] == inputArray[x][y] + 1:
                    recursiveGetScore(inputArray, new_x, new_y, endSets)
    recursiveGetScore(inputArray, x, y, endSets)
    return len(endSets)    

def getRating(inputArray: list[list[int]], 
                x: int, 
                y: int,
                ) -> int:
    if inputArray[x][y] == 9:
        return 1
    final = 0
    for a, b in [(-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)]:
        new_x = x + a
        new_y = y + b
        if 0 <= new_x < len(inputArray) and 0 <= new_y < len(inputArray[0]):
            if inputArray[new_x][new_y] == inputArray[x][y] + 1:
                final += getRating(inputArray, new_x, new_y)
    return final

def countPathRating(inputArray: list[list[int]]):
    total = 0
    starts = getStarts(inputArray)
    # print(starts)
    for start in starts:
        print(start)
        total += getRating(inputArray, start[0], start[1])
    return total

def countPaths(inputArray: list[list[int]]):
    total = 0
    starts = getStarts(inputArray)
    # print(starts)
    for start in starts:
        print(start)
        total += getScore(inputArray, start[0], start[1])
    return total

if __name__ == '__main__':
    inputArray = getInputArray('./day10/input2.txt')
    # [print(i) for i in inputArray]
    print(countPaths(inputArray))
    print(countPathRating(inputArray))
    # out1 = getPrearrangeRep(inputArray)
    # # print(out1)
    # # out2 = rearrangeWholeFile(out1)
    # out2 = rearrangeString(out1)
    