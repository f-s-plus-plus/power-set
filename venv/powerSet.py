import copy
def powerSet(entryArray):
    finalArray = [[]]
    length = 2 ** len(entryArray);
    for value in range(length):
        for entry in entryArray:
            temp = copy.deepcopy(finalArray[value])
            if entry not in temp:
                temp.append(entry)
            temp = sorted(temp)
            if temp not in finalArray:
                finalArray.append(temp)
    return finalArray


c = powerSet(["1","2"])
print(c)