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
    pattern = r"([<>]*)([v\^]*)(A)"
    a = re.match(pattern, val)
    return a.group(2) + a.group(1) + 'A'



    

def initNumToDirArrowDict():
    """
    For each key on keypad, returns string for shortest path of arrow buttons
    on direcitonal keypad to get to new number

    Counts press of the A button
    """

    numDirDict: dict[tuple[str, str], int] = {}

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
                        grid_diff_str = GRID_DIFF_TO_STRING[(x1, y1)]
                        # if x == 3:
                        #     grid_diff_str = switchStr(grid_diff_str)
                        #     print(a, b)
                        #     print(grid_diff_str)
                        #     print()
                            
                        numDirDict[(a, b)] = grid_diff_str
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
                        grid_diff_str = GRID_DIFF_TO_STRING[(x1, y1)]
                        if x == 0:
                            grid_diff_str = switchStr(grid_diff_str)
                            # print(a, b)
                            # print(grid_diff_str)
                            # print()
                        
                        dirDirDict[(a, b)] = grid_diff_str
    return dirDirDict    
      

def processCode(code: str)-> str:
    # print(code)
    newStrList = []
    codeInt = int(code.lstrip('0').rstrip('A'))
    code = 'A' + code
    for i in range(len(code)):    
        if i + 1 < len(code):
            outStr = NUM_DIR_DICT[(code[i], code[i + 1])]

            # TODO: Update so that NUM_DIR_DICT returns 
            # one option if going along one axis only (i.e., 0, 1 or 3, 0)
            # if diff b/t two cells is on both axes, try <<<^^^^ vs ^^^^<<< (one axes first hten other)
            # then need to add to list of multiple possible strings
            # so if going from 2 to 9,
            #    ^^> is appended and goes in a list
            #    >^^ is appended and goes in another list
            newStrList.append(outStr)
    newStr = ''.join(newStrList)
    print(newStr)
    # print(newStr)

    # newStrList1 = []
    # code = 'A' + newStr
    # # print(code)
    # for i in range(len(code)):    
    #     if i + 1 < len(code):
    #         outStr = DIR_DIR_DICT[(code[i], code[i + 1])]
    #         newStrList1.append(outStr)
    # newStr = ''.join(newStrList1)
    
    # newStrList2 = []
    # code = 'A' + newStr
    # for i in range(len(code)):    
    #     if i + 1 < len(code):
    #         outStr = DIR_DIR_DICT[(code[i], code[i + 1])]
    #         newStrList2.append(outStr)
    # newStr = ''.join(newStrList2)
    # print(len(newStr)) 
    # print(codeInt)
    # return len(newStr) * codeInt
    return 0
        
    

def processCodes(code: str) -> str: 
    total = 0
    for code in codes[:1]:
        total += processCode(code)
    return total


if __name__ == '__main__':
    inputArray = getInput('./day21/input0.txt')
    codes = [i.strip() for i in inputArray]
    GRID_DIFF_TO_STRING = gridDiffToString()
    # print(inputArray)
    NUM_DIR_DICT = initNumToDirArrowDict()
    DIR_DIR_DICT = initDirToDirArrowDict()
    print(processCodes(codes))
    # switchStr('<vA')
    # for code in codes:
    #     processCodes(code)
    # print(codes)
    # grid = processInput(inputArray)


# A<<vAA>^A>A<AA>AvAA^A<vAAA>^A