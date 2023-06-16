

import heapq

def instert(intervals, newInterval):
    result = []
    bail_index = len(intervals)
    for i in range(len(intervals)):
        if intervals[i][1] < newInterval[0]: #no overlap
            result.append(intervals[i])
        else:
            bail_index = i
            break
    result.append(newInterval)
    for i in range(bail_index, len(intervals)):
        if result[-1][1] < intervals[i][0]: #no overlap
            result.append(intervals[i])
        else: #overlap
            result[-1] = [min(result[-1][0], intervals[i][0]),
                          max(result[-1][1], intervals[i][1])]
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