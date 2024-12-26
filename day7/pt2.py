def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def processLine(arr: str, useConcatOperator: bool) -> int:
    linesplit = line.split(':')
    ans, operands = int(linesplit[0]), linesplit[1]
    operands = [int(i) for i in operands.strip().split(' ')]
    values = [operands[0]]
    for operand in operands[1:]:
        newValues = []
        for value in values:
            if useConcatOperator:
                newValues.append(int(str(value) + str(operand)))
            newValues.append(value + operand)
            newValues.append(value * operand)
        values = newValues
    if ans in set(newValues):
        return ans
    return 0      

if __name__ == '__main__':
    inputArray = getInput('./day7/input1.txt')
    sum = 0
    for line in inputArray:
        sum += processLine(line, useConcatOperator= True)
    print(sum)
    # processLines(inputArray)