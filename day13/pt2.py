from collections import defaultdict
import re

def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def getEquations(inputArray: list[str]) -> list[dict[str, list[int]]]:
    currEquation = None
    equations = []
    for i in range(len(inputArray)):
        if len(inputArray[i].strip()) > 0:
            if inputArray[i].startswith('Button A'):
                if currEquation:
                    equations.append(currEquation)
                currEquation = defaultdict(list)
            x = int(re.search(r"X[\+=]([0-9]*)", inputArray[i]).group(1))
            y = int(re.search(r"Y[\+=]([0-9]*)", inputArray[i]).group(1))
            if inputArray[i].startswith('Prize'):
                x += 10000000000000
                y += 10000000000000
            currEquation['x'].append(x)
            currEquation['y'].append(y)
    equations.append(currEquation)
    return equations

def solveEquation(equation: dict[str, list[int]]) -> tuple[int, int]:
    e = equation
    constants = e['y'][2] - (e['y'][1] * e['x'][2] / e['x'][1])
    aconstant = e['y'][0] - e['y'][1] * e['x'][0] / e['x'][1]
    a = constants / aconstant
    b = (e['x'][2] - e['x'][0] * a) / e['x'][1]
    return a, b
    

if __name__ == '__main__':
    inputArray = getInput('./day13/input1.txt')
    
    a = getEquations(inputArray)
    total = 0
    for equation in a:
        a, b = solveEquation(equation)
        if abs(a - (round(a))) < 0.001:
            total += a * 3 + b
        else:
            print(a, b)
