
def intervalIntersection(firstList, secondList):
    #in this problem we will use 2 pointers technique
    i = 0
    j = 0
    result = []

    while i < len(firstList) and j < len(secondList):
        #if first list meeting ends before second list meeting start increment, then there is no overlap, you need to increment i
        if firstList[i][1] < secondList[j][0]:
            i+=1
        #If second list meeting ends before first list meeting start, then there is no overlap, increment j
        elif secondList[j][1] < firstList[i][0]:
            j += 1
        #otherwise there is overlap from the max start and min end of both meeting.
        else:
            result.append([max(firstList[i][0], secondList[j][0]),
                          min(firstList[i][1], secondList[i][1])])
            #you need to move away from the smallest end, as the longer meeting can overlap with next meeting from the other list
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
    return result

def test():
    min_heap = [-1,-2,-3,-4,-5]
    max_heap = [6,7,8,9,10]

    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    print(min_heap)
    print(max_heap)

    print(heapq.heappop(min_heap))
    print(heapq.heappop(max_heap))