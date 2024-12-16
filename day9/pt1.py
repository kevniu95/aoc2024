def getInputString(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def getPrearrangeRep(input: str) -> list[int]:
    outputStringList = []
    for num, char in enumerate(input):
        value = num // 2 if num % 2 == 0 else None
        for i in range(int(char)):
            outputStringList.append(value)
    return outputStringList
    
def rearrangeString(input: list[int]) -> list[int]:
    l = 0
    r = len(input) - 1
    while l < r:
        while input[l] is not None:
            l += 1
        while input[r] is None:
            r -= 1
        # print(l ,r)
        input[r], input[l] = input[l], input[r]
        l += 1; r -= 1
    return input

def calcValue(input: str) -> str:
    sum = 0
    for num, i in enumerate(input):
        if i:
            sum += num * int(i)
    return sum

def findBlankSpaceOfTargetLength(input: list[int],
                                 l: int,
                                 r: int) -> int:
    pass

def findRightMostContiguousNumbers(input: list[int],
                                   l: int,
                                   r: int) -> tuple[int, int]:
    while input[r] is None:
        r -= 1
    current_r = input[r]
    r_r = r
    while input[r] == current_r:
        r -= 1
        if r == 0:
            return 0, r_r
    return r + 1, r_r

def findFirstLeftSpace(input: list[int],
                       end: int,
                       targetLength: int) -> tuple[int, int]:
    l = 0
    r = 0
    while l < end:
        while input[l] is not None and l < end:
            l += 1
        r = l
        while input[r] is None:
            r += 1
        r -= 1
        currLength = r - l + 1
        # print(currLength)
        if currLength >= targetLength:
            return l, r
        l += 1
    return None, None

def rearrangeWholeFile(input: list[int]) -> list[int]:
    l = 0
    r = len (input) - 1
    while r > 0:
        r_l, r_r = findRightMostContiguousNumbers(input, l, r)
        targetLength = (r_r - r_l + 1)
        l_l, l_r = findFirstLeftSpace(input, r_l, targetLength)
        if l_l and l_r:
            for i in range(targetLength):
                # print(f"Swapping {l_l+ i} and {r_l + i}")
                input[l_l + i], input[r_l + i] =  input[r_l + i], input[l_l + i]
        r = r_l - 1
    return input
    


if __name__ == '__main__':
    inputArray = getInputString('./day9/input1.txt')
    out1 = getPrearrangeRep(inputArray)
    # print(out1)
    # out2 = rearrangeWholeFile(out1)
    out2 = rearrangeString(out1)
    
    print(out2)
    print(calcValue(out2))
 
 
    # print(out2)
    # assert len(out1) == len(out2)
    
    # print(out2)
    
    # print(out2)
    # print(out2)
    #  '0099811188827773336446555566..............'

  #  '00...111...2...333.44.5555.6666.777.888899'
  #  '0099811188827773336446555566..............'