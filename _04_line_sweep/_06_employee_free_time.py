#https://leetcode.com/problems/employee-free-time/
#759. Employee Free Time
import heapq


def employee_free_time(schedule):
    result = [[float('-inf'), float('-inf')]]
    pq = []
    for eindex in range(len(schedule)):
        if len(schedule[eindex]) > 0:
            heapq.heappush(pq, (schedule[eindex][0][0], eindex, 0))
    while len(pq) > 0:
        (start, eindex, pos) = heapq.heappop(pq)
        if result[-1][1] < start:  # no overlap
            result.append(schedule[eindex][pos])
        else:  # overlap
            result[-1] = [result[-1][0], max(result[-1][1], schedule[eindex][pos][1])]
        print(result)
        pos += 1
        if pos < len(schedule[eindex]):
            heapq.heappush(pq, (schedule[eindex][pos][0], eindex, pos))

    free_time = []
    for i in range(1, len(result) - 1):
        free_time.append([result[i][1], result[i + 1][0]])
    return free_time


def test():
    # schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]  #[(3,4)]
    schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]  # [(5,6),(7,9)]
    result = employee_free_time(schedule)
    print(result)
