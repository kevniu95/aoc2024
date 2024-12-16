def getInputFile(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def processFile(file: list[str]) -> list[list[str]]:
    finalArr = []
    for line in file:
        line = line.strip()
        finalArr.append([i for i in line])
    return finalArr

def getInitialPosition(arr: list[list[str]],
                       arrowSet = ['<','>', 'v', '^']
                       ) -> tuple[int, int, str]:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] in arrowSet:
                return i, j, arr[i][j]

arrowMapper = {
    '<' : (0, -1),
    '>' : (0, 1),
    'v' : (1, 0),
    '^' : (-1, 0)
}

rightTurnMapper = {
    '<' : '^',
    '^' : '>',
    '>' : 'v',
    'v' : '<'
}

def traverseArray(arr: list[list[str]]) -> int:
    seenSet = set()
    x, y, arrowVal = getInitialPosition(arr)
    arr[x][y] = '.'
    i = 0
    while 0 <= x < len(arr) and 0 <= y < len(arr[0]):
        i += 1
        moveDirection = arrowMapper[arrowVal]
        seenSet.add((x, y))
        x_1, y_1 = x + moveDirection[0], y + moveDirection[1]
        if x_1 < 0 or x_1 >= len(arr) or y_1 < 0 or y_1 >= len(arr[0]):
            return len(seenSet)
        elif arr[x_1][y_1] == '.':
            x, y = x_1, y_1
        elif arr[x_1][y_1] == '#':
            arrowVal = rightTurnMapper[arrowVal]
    return len(seenSet)

def traverseArray(arr: list[list[str]]) -> int:
    seenSet = set()
    x, y, arrowVal = getInitialPosition(arr)
    arr[x][y] = '.'
    i = 0
    while 0 <= x < len(arr) and 0 <= y < len(arr[0]):
        i += 1
        moveDirection = arrowMapper[arrowVal]
        seenSet.add((x, y))
        x_1, y_1 = x + moveDirection[0], y + moveDirection[1]
        if x_1 < 0 or x_1 >= len(arr) or y_1 < 0 or y_1 >= len(arr[0]):
            return len(seenSet)
        elif arr[x_1][y_1] == '.':
            x, y = x_1, y_1
        elif arr[x_1][y_1] == '#':
            arrowVal = rightTurnMapper[arrowVal]
    return len(seenSet)

if __name__ == '__main__':
    inputFile = getInputFile('./day6/input1.txt')
    inputFile = processFile(inputFile)
    print(traverseArray(inputFile))
    