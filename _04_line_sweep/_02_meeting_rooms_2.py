#https://leetcode.com/problems/meeting-rooms-ii/solutions/67855/Explanation-of-%22Super-Easy-Java-Solution-Beats-98.8%22-from-@pinkfloyda/

import heapq


def meeting_rooms_2(intervals):
    intervals.sort(key=lambda x:x[0])
    next_start:int
    min_heap = []
    gmax = 0
    for i in range(len(intervals)):
        if i == len(intervals) - 1:
            next_start = float('INF')
        else:
            next_start = intervals[i+1][0]
        heapq.heappush(min_heap, intervals[i][1])
        gmax = max(gmax,len(min_heap))
        #print(min_heap, next_start)
        while len(min_heap) > 0 and min_heap[0] <= next_start:
            heapq.heappop(min_heap)
    return gmax

def test():
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(meeting_rooms_2(intervals))
