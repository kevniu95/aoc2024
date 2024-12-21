def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def processInput(inputArray: list[str]) -> tuple[list[list[int]], list[int]]:
    total = 0
    for line in inputArray:
        total += processLine(line)
        print()
    return total

def processLine(line: str) -> int:
    l = 0
    total = 0
    do = 1
    while l < len(line):
        firstNum = 0
        secondNum = 0
        print(line[l : l +7])
        if line[l: l + 4] == 'do()':
            l = l + 4
            do = 1
        if line[l: l + 7] == "don't()":
            l = l + 7
            do = 0
        if line[l: l + 4] ==  'mul(':
            l = l + 4
            while '0' <= line[l] <= '9':
                firstNum = firstNum * 10 + int(line[l])
                l += 1
            if line[l] == ',':
                l += 1
                while '0' <= line[l] <= '9':
                    secondNum = secondNum * 10 + int(line[l])
                    l += 1
                if line[l] == ')':
                    print(f"Adding product of {firstNum} and {secondNum}: {firstNum * secondNum} to total")
                    print(f"do value is {do}")
                    total += do * firstNum * secondNum
                    
        l += 1
    return total

if __name__ == '__main__':
    inputArray = getInput('./day3/input1.txt')
    inputStr = ''.join(inputArray)
    