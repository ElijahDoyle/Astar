import random

def lowestFcost(inputList):
    lowestValue = None
    lowList = []
    for index, i in enumerate(inputList):
        if lowestValue == None:
            lowestValue = i.f
        if i.f == lowestValue:
            lowList.append(index)
        elif i.f < lowestValue:
            lowList = [index]
            lowestValue = i.f
    if len(lowList) == 1:
        return lowList[0]
    else:
        lowestH = inputList[lowList[0]].h
        bestIndex = lowList[0]
        for index in lowList:
            currentNode = inputList[index]
            currentH = currentNode.h
            if currentH < lowestH:
                bestIndex = index
                lowestH = inputList[index].h

        return bestIndex