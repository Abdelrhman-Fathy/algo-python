#Problem 7 - Interval List Intersections (986)
def intervalIntersection(firstList, secondList):
    i = 0
    j = 0
    result = []
    while i < len(firstList) and j < len(secondList):
        if firstList[i][1] < secondList[j][0]: #no overlap
            i+=1
        elif secondList[j][1] < firstList[i][0]: #no overlap
            j +=1
        else: #overlap
            result.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if firstList[i][1] <= secondList[j][1]:
                i+=1
            else:
                j+=1
    return result



def test():
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    result = intervalIntersection(firstList, secondList)
    print(result)