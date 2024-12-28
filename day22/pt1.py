from collections import defaultdict

def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()    
    return data


def processInput(data: list[str]) -> list[list[str]]:
    secretNumbers = []
    for line in data:
        secretNumbers.append(int(line.strip()))
    return secretNumbers

def getNewSecretNumber(num: int) -> int:
    num = (num * 64)^num
    num %= 16777216
    num = (num // 32) ^ num
    num %= 16777216
    num = (num * 2048)^num
    num %= 16777216
    return num
    

if __name__ == '__main__':
    data = getInput('./day22/input3.txt')
    secretNumbers = processInput(data)
    
    N = 2000
    nth_numbers = []
    for secretNumber in secretNumbers:
        for i in range(N):
            secretNumber = getNewSecretNumber(secretNumber)
        nth_numbers.append(secretNumber)
    print(sum(nth_numbers))
            
            

    # print(processNumber(secretNumbers[0]))
    # print(getNewSecretNumber(123))



    # start, end = getStart(grid)
    # print(start, end)

    # path_cells: list[tuple[int, int]] = []
    # cell_dict: dict[tuple[int, int], int] = {}
    # cheat_dict: dict[tuple[int, int], int] = defaultdict(list)
    
    
    # walkPath(grid, start, end, path_cells, cell_dict)

    # cheat_dict = evaluateCheats(grid, start, end, path_cells, cell_dict, cheat_dict)
    
    # finalList = []
    # for k, v in cheat_dict.items():
    #     finalList.extend([i for i in v if i >= 100])
    # print(len(finalList))