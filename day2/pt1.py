
def getInputArray(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as file:
      data = file.readlines()

    bigArray = []
    for line in data:
        line = line.strip()
        currArray = []
        for item in line.split(' '):    
            currArray.append(int(item)
                            )
        bigArray.append(currArray)
    return bigArray
        

def checkLineSafe(inputLine: list[int]) -> bool:
    lastValue = None
    switch = None
    for i in inputLine:
        if lastValue:
            if not switch:
                switch = 1 if i > lastValue else -1
            if not 1 <= (i - lastValue) * switch <= 3:
                return False
        lastValue = i
    return True
        
def getSafeLines(inputArray) -> int:
    total = 0
    for line in inputArray:
        total += checkLineSafe(line)
    return total


def checkLineSafeHard(inputLine: list[int]) -> bool:
    if checkLineSafe(inputLine) or checkLineSafe(inputLine[1:]):
        return True
    lastValue = None
    switch = None
    for i, val in enumerate(inputLine):
        if lastValue:
            if not switch:
                switch = 1 if val > lastValue else -1
            if not 1 <= (val - lastValue) * switch <= 3:
                return checkLineSafe(inputLine[:i - 1] + inputLine[i:]) or checkLineSafe(inputLine[:i] + inputLine[i + 1:])
        lastValue = val
    return True
    
    
def getSafeLinesHard(inputArray) -> int:
    total = 0
    for enum, line in enumerate(inputArray):
        print(f"Processing line: {enum + 1}")
        total += checkLineSafeHard(line)
    return total

if __name__ == "__main__":
    inputArray = getInputArray('./day2/input.txt')
    # print(getSafeLines(inputArray))
    print(getSafeLinesHard(inputArray))