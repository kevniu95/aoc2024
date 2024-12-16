from pt1 import l1, l2
# l1 = [3,
# 4,
# 2,
# 1,
# 3,
# 3]

# l2 = [4,
# 3,
# 5,
# 3,
# 9,
# 3]

def getCountOfKeys(l: list[int]):
    countDict = {}
    for i in l:
        if i in countDict:
            countDict[i] += 1
        else:
            countDict[i] = 1
    return countDict

def getSimilarityScore(
    l1: list[int], 
    l2: list[int]
    ) -> int:
    simScore = 0
    countDict2 = getCountOfKeys(l2)
    
    for i in range(len(l1)):
        added = l1[i] * countDict2.get(l1[i], 0)
        simScore += added
    
    return simScore


if __name__ == "__main__":
    print(getSimilarityScore(l1, l2))