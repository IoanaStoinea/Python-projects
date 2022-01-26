def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size - 1] = temp

    return  newList

newList = [1,2,3,5,6,7,8]
print(newList)
print(swapList(newList))

list = [10,122,22,44,5,6]
print(swapList(list))
