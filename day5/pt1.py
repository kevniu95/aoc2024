from collections import defaultdict

def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def processInput(lines:str) -> tuple[list[str], list[str]]:
    rules = []
    updates = []
    for line in lines:
        if '|' in line:
            rules.append(line)
        elif ',' in line:
            updates.append(line)
    return rules, updates
            
def saveRulesDict(rules: list[str]):
    rulesDict : dict[str, set[str]] = defaultdict(set)
    for rule in rules:
        a, b = rule.split('|')
        rulesDict[a].add(b)
    return rulesDict      

def isCorrect(update : str) -> bool:
    entries = update.split(',')
    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            if entries[j] not in RULES_DICT[entries[i]]:
                return False
    return True

def middleOfCommaSepString(val: str) -> int:
    arr = val.split(',')
    return int(arr[len(arr) // 2])
    
    


if __name__ == '__main__':
    input = getInput('./day5/input1.txt')
    rules, updates = processInput(input)
    RULES_DICT = saveRulesDict(rules)
    for k, v in RULES_DICT.items():
        print(k)
        print(len(v))
        print()

    # total = 0
    # for update in updates:
    #     if isCorrect(update):
    #         total += middleOfCommaSepString(update)
    # print(total)
            
            
    # print(rules)
    # print(updates)
    # print(countXmas(grid))
    # print(grid)
