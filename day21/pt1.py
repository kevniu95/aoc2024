import math
import re 
def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def gridDiffToString() -> str: 
    """
    For every x, y representing diff in x, y coords b/t two points in grid,
    return theh string represnting how to get from pt A to pt B in string form
    """
    dirDict: dict[tuple[int, int], str] = {}
    for i in range(-3, 4):
        for j in range(-3, 4):
            row_dir = '^' if i < 0 else 'v'
            col_dir = '<' if j < 0 else '>'
            final_str = row_dir * abs(i) + col_dir * abs(j)
            dirDict[(i, j)] = final_str + 'A'
    return dirDict
            
def switchStr(val: str):
    try:
        pattern = r"([v\^]*)([<>]*)(A)"
        a = re.match(pattern, val)
        return a.group(2) + a.group(1) + 'A'
    except:
        return val

def initNumToDirArrowDict():
    """
    For each key on keypad, returns string rep of possible paths
          
    Counts press of the A button
    """

    numDirDict: dict[tuple[str, str], list[str]] = {}

    grid = [['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            [None, '0', 'A']]
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[x][y] and grid[i][j]:
                        a, b = grid[x][y], grid[i][j]
                        x1, y1 = i - x, j - y
                        inputArr = []
                        grid_diff_str = GRID_DIFF_TO_STRING[(x1, y1)]
                        inputArr.append(grid_diff_str)
                        grid_diff_str_2 = switchStr(grid_diff_str)
                        if grid_diff_str_2 != grid_diff_str:
                            inputArr.append(grid_diff_str_2)
                        if (y == 0 ) and len(inputArr) > 1:
                            inputArr.pop(0)
                        if (j == 0 and x == 3) and len(inputArr) > 1:
                            inputArr.pop(1)
                        numDirDict[(a, b)] = inputArr
    return numDirDict
              
                    
def initDirToDirArrowDict():
    """
    For each key on direction pad, returns string for shortest path of dir buttons
    on direcitonal keypad to get to new number

    Counts press of the A button
    """
    grid = [[None, '^', 'A'],
            ['<', 'v', '>']]
    
    dirDirDict = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[x][y] and grid[i][j]:
                        a, b = grid[x][y], grid[i][j]
                        x1, y1 = i - x, j - y
                        inputArr = []
                        grid_diff_str = GRID_DIFF_TO_STRING[(x1, y1)]
                        inputArr.append(grid_diff_str)
                        grid_diff_str_2 = switchStr(grid_diff_str)
                        if grid_diff_str_2 != grid_diff_str:
                            inputArr.append(grid_diff_str_2)                        
                        if (y == 0) and len(inputArr) > 1:
                            inputArr.pop(0)
                        if (j == 0 and x == 0) and len(inputArr) > 1:
                            inputArr.pop(1)  
                        dirDirDict[(a,b)] = inputArr
    return dirDirDict    

def reduceList(myList: list[str]) -> list[str]:
    lengths = [len(line) for line in myList]
    minLength = min(lengths)
    finalList = []
    for line in myList:
        if len(line) == minLength:
            finalList.append(line)
    return finalList


def convertCodeToListOfCodes(code: str, myDict : dict = None):
    if not myDict:
        myDict = DIR_DIR_DICT
    strList = ['']
    for i in range(len(code)):
        if i + 1 < len(code):
            outStr = myDict[(code[i], code[i + 1])]
            newStrList = []
            for x in range(len(strList)):
                for y in range(len(outStr)):
                    newStrList.append(strList[x] + outStr[y])
            strList = newStrList
    return strList
            

def processCode(code: str)-> str:
    print(f"Procesing code {code}")
    strList = ['']
    codeInt = int(code.lstrip('0').rstrip('A'))
    codes = [code]
    codes = ['A' + code for code in codes]
    newCodes = []
    for code in codes:
        aNewCode = convertCodeToListOfCodes(code, NUM_DIR_DICT)
        newCodes.extend(aNewCode)
    
    codes = ['A' + code for code in reduceList(newCodes)]
    
    newCodes = []
    for code in codes:
        aNewCode = convertCodeToListOfCodes(code, DIR_DIR_DICT)
        newCodes.extend(aNewCode)
    codes = ['A' + code for code in newCodes]
    
    newCodes = []
    for code in codes:
        aNewCode = convertCodeToListOfCodes(code, DIR_DIR_DICT)
        newCodes.extend(aNewCode)
    codes = [code for code in reduceList(newCodes)]
    # print(codes)
    print("Code lengths")
    print(len(codes[0]))
    print(codeInt)
    return len(codes[0]) * codeInt
        
    

def processCodes(code: str) -> str: 
    print("PRocessing all codes")
    total = 0
    for code in codes:
        total += processCode(code)
    return total

if __name__ == '__main__':
    inputArray = getInput('./day21/input1.txt')
    codes = [i.strip() for i in inputArray]
    GRID_DIFF_TO_STRING = gridDiffToString()
    # print(inputArray)
    NUM_DIR_DICT = initNumToDirArrowDict()
    print(NUM_DIR_DICT)
    DIR_DIR_DICT = initDirToDirArrowDict()
    print()
    print(DIR_DIR_DICT)
    print(processCodes(codes))