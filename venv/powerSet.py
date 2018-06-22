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

def powerset(n):
    final = [[]]
    def powerset_helper(array, org_array, index):
        i = index
        while i < len(org_array):
            list_tmp = copy.deepcopy(array)
            list_tmp.append(org_array[index])
            final.append(list_tmp)
            i += 1
            powerset_helper(list_tmp, org_array, i)
    
    powerset_helper([], n, 0)
    return final 

c = powerSet(["1","2"])
print(c)
