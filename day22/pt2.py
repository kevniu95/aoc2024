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

def processNumber(secretNumber: int) -> None:
    tupleSeenSet = set()
    priceList = [secretNumber % 10]
    priceDiffList = [None]
    for j in range(N):
        oldSecretNumber = secretNumber
        secretNumber = getNewSecretNumber(secretNumber)
        oldPrice = oldSecretNumber % 10
        price = secretNumber % 10
        
        priceList.append(secretNumber % 10)
        priceDiff = price - oldPrice
        priceDiffList.append(priceDiff)
        if j >= (PRICE_DIFF_SEQ_LEN - 1):
            tup = tuple(priceDiffList[-4:])
            if tup not in tupleSeenSet:
                BIG_DICT[tup] = BIG_DICT.get(tup, 0) + price
                tupleSeenSet.add(tup)



if __name__ == '__main__':
    data = getInput('./day22/input2.txt')
    secretNumbers = processInput(data)
    N = 2000
    PRICE_DIFF_SEQ_LEN = 4
    nth_numbers = []
    prices = []
    BIG_DICT : dict[tuple[int, int, int, int], int]= {}
    for secretNumber in secretNumbers:
        processNumber(secretNumber)
        
    print(BIG_DICT)

    print({k: v for k, v in sorted(BIG_DICT.items(), key=lambda item: item[1])})