
from collections import deque

def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()    
    return data

def processInput(data: list[str]) -> tuple[list[str], list[str]]:
    designs = []
    for i in range(len(data)):
        if i == 0:
            line = data[i].strip()
            patterns = [i.strip() for i in line.split(',')]

        if i > 1:
            designs.append(data[i].strip())
    return patterns, designs
            

def checkDesign(design: str, patterns: list[str], ) -> bool:
    if design in DESIGN_DICT:
        return DESIGN_DICT[design]
    if design == '':
        return True
    hasPath = False
    for pattern in patterns:
        if design.startswith(pattern):
            newStr = design.removeprefix(pattern)
            hasPath = hasPath or checkDesign(newStr, patterns)
    DESIGN_DICT[design] = hasPath
    return hasPath
            
if __name__ == '__main__':
    data = getInput('./day19/input1.txt')
    patterns, designs = processInput(data)

    goodDesigns = 0
    DESIGN_DICT = {}
    for design in designs:
        designGood = checkDesign(design, patterns)
        print(designGood)
        goodDesigns += designGood
    print(goodDesigns)
        
        
    