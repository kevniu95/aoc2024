def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.read()
    # out = []
    # for line in data:
    #     out.append([int(j) if '0' <= j <= '9' else j for j in line.strip()])
    # return out
    return data

def blink(init : list[int]) -> str:
    out = []
    for i in init:
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

if __name__ == '__main__':
    inputArray = getInput('./day11/input0.txt')
    inputArray = '8'
    initArray = [int(i) for i in inputArray.split(' ')]
    for i in range(5):
        # print(i)
        # print(initArray)
        initArray = blink(initArray)
        # print(initArray)
    print(initArray)
    print(len(initArray))
    # [print(i) for i in inputArray]
    # print(countPaths(inputArray))
    # print(countPathRating(inputArray))