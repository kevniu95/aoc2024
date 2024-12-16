def getInputFile(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def processFile(file: list[str]) -> list[list[str]]:
    finalArr = []
    for line in file:
        line = line.strip()
        finalArr.append([Square(i, set()) for i in line])
    return finalArr

class Square():
    def __init__(self, val: str, flags = set[str]):
        self.val = val
        self.flags = flags
    
    def __str__(self):
        return self.val + ":" + str([i for i in self.flags])
        
    def __repr__(self):
        return self.val + ":" + str([i for i in self.flags])

def getInitialPosition(arr: list[list[Square]],
                       arrowSet = ['<','>', 'v', '^']
                       ) -> tuple[int, int, str]:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            char_val = arr[i][j].val
            if char_val in arrowSet:
                return i, j, char_val
            
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

def fillFlags(arr: list[list[Square]], 
              x: int, 
              y: int, 
              arrowVal: str
              ) -> None:
    currentTravelDirection = rightTurnMapper[rightTurnMapper[arrowVal]]
    valueToSave = rightTurnMapper[currentTravelDirection]
    while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y].val != '#':
        arr[x][y].flags.add(valueToSave)
        moveDirection = arrowMapper[currentTravelDirection]
        x, y = x + moveDirection[0], y + moveDirection[1]



def traverseArray(arr: list[list[Square]]) -> int:
    seenSet = set()
    x, y, arrowVal = getInitialPosition(arr)
    arr[x][y].val = '.'
    i = 0
    loops = 0
    while 0 <= x < len(arr) and 0 <= y < len(arr[0]):
        i += 1
        moveDirection = arrowMapper[arrowVal]
        seenSet.add((x, y))
        x_1, y_1 = x + moveDirection[0], y + moveDirection[1]
        if arrowVal in arr[x][y].flags and 0 <= x_1 < len(arr) and 0 <= y_1 < len(arr[1]):
            print("Adding to loops")
            loops += 1
        if x_1 < 0 or x_1 >= len(arr) or y_1 < 0 or y_1 >= len(arr[0]):
            return loops
        elif arr[x_1][y_1].val == '.':
            x, y = x_1, y_1
        elif arr[x_1][y_1].val == '#':
            fillFlags(arr, x, y, arrowVal)
            arrowVal = rightTurnMapper[arrowVal]
    return loops

if __name__ == '__main__':
    inputFile = getInputFile('./day6/input1.txt')
    inputFile = processFile(inputFile)
    # print(traverseArray(inputFile))
    for i in inputFile:
        print([j for j in i])
    