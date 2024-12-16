def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.read()
    # out = []
    # for line in data:
    #     out.append([int(j) if '0' <= j <= '9' else j for j in line.strip()])
    # return out
    return data



def setSingleDigitDict():
    finalDict = {}
    for i in range(0, 1):
        curr_list = [i]
        
        all_i_list_len_1 = all([0 <= i < 10 for i in curr_list])
        j = 0
        while len(curr_list) <= 1 or not all_i_list_len_1:
            print(j)
            print(curr_list)
            curr_list = blink(curr_list)
            all_i_list_len_1 = all([0 <= i < 10 for i in curr_list])
            j += 1
            finalDict[(i, j)] = len(curr_list)
            
        print(j)
        print(curr_list)
        print(finalDict)
            

def doBlinks(initArray: list[int], num: int) -> int:
    setSingleDigitDict()
    # seenSet = {}
    # for i in range(num):
    #     blink(initArray)
    # return len(seenSet)



def fillDpTable(specialNumbers: dict[list, int], cols: int = 10):
    dp = []
    for i in range(10):
        currRow = []
        for j in range(cols):
            currRow.append(None)
        dp.append(currRow)


    # Fill first 6 columns
    for i in range(10):
        blinkInput = [i]
        ind = 0
        for j in range(6):
            dp[i][ind] = len(blinkInput)
            blinkInput = blink(blinkInput)
            ind += 1
    
    # [print(i) for i in specialNumbers.values()]
    for col in range(6,cols):
        for i in range(10):
            val = 0
            special = specialNumbers[i][0]
            start = specialNumbers[i][1]
            for sp in special:
                x, y = sp[0], sp[1] + (col - start)
                val += dp[x][y]
            dp[i][col] = val
          
    return dp
    
        
def blink(init : list[int]) -> str:
    out = []
    for i in init:
        if not isinstance(i, int):
            i[1] += 1
            out.append(i)
            continue
        if i == 0:
            out.append(1)
        elif len(str(i)) % 2 == 0:
            str_i = str(i)
            mid = len(str(i)) // 2
            lh = str_i[:mid]
            rh = str_i[mid:]
            out.append(int(lh))
            out.append(int(rh))
        else:
            out.append(i * 2024)
    return out

def blinkToSetupSpecialNumber():
    out = {}
    for i in range(10):
        arr = [i] # O blinks
        blinks = 0
        for j in range(5):
            arr = blink(arr)
            for k in range(len(arr)):
                if isinstance(arr[k], int) and 0 <= arr[k] <= 9 and len(arr) > 1:
                    arr[k] = [arr[k], 0]
            blinks += 1
            if all([not isinstance(k, int) for k in arr]):
                if i not in out:
                    out[i] = (arr.copy(), blinks)
                break
    return out
              
if __name__ == '__main__':
    inputArray = getInput('./day11/input1.txt')
    specialNumbers = blinkToSetupSpecialNumber()
    # [print(k) for k in specialNumbers.values()]
    dpTable = fillDpTable(specialNumbers, 75)
    [print(k) for k in dpTable]

    initArray = [int(i) for i in inputArray.split(' ')]
    for i in range(75):
        initArray = blink(initArray)
        for i in range(len(initArray)):
            if isinstance(initArray[i], int) and 0 <= initArray[i] <= 9:
                initArray[i] = [initArray[i], 0]
            
    
    count = 0
    for i in initArray:
        if isinstance(i, int):
            count += 1
        else:
            count += dpTable[i[0]][i[1]]
    
    print(count)
        # print()
    # setSingleDigitDict()
    # initArray = [int(i) for i in inputArray.split(' ')]
    # for i in range(75):
    #     print(i)
    #     initArray = blink(initArray)
    #     # print(initArray)
    # print(initArray)
    # print(len(initArray))
    # [print(i) for i in inputArray]
    # print(countPaths(inputArray))
    # print(countPathRating(inputArray))