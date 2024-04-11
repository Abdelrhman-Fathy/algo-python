#https://leetcode.com/problems/employee-free-time/
#759. Employee Free Time
import heapq
def employee_free_time(schedule):
    #I intialized the meetings array not to be empty, I added one default meeting that start and end in -inf point of time hence it will not overlap with any meeting in our test data.
    meetings = [[float('-inf'), float('-inf')]]
    heap = []
    #put first schedule from each employee in a heap

    for empIndex in range(len(schedule)):
        if len(schedule[empIndex]) > 0:
            heapq.heappush(heap, (schedule[empIndex][0][0], empIndex, 0))
    #keep removing from the heap the earliest schedule and when you remove one schedule from the heap you need to add another schedule from the same employee.
    while len(heap) > 0:
        (start, empIndex, meetingIndex) = heapq.heappop(heap)
        if len(schedule[empIndex]) > meetingIndex + 1:
            heapq.heappush(heap, (schedule[empIndex][meetingIndex+1][0], empIndex, meetingIndex+1))

        #if current meeting not overlapping with previous meeting add it
        # else change the end time of previous meeting to be max of current meeting and previous meeting, i.e merge them

        if meetings[-1][1] < start:
            meetings.append(schedule[empIndex][meetingIndex])
        else:
            meetings[-1][1] = max(meetings[-1][1], schedule[empIndex][meetingIndex][1])
    #free time is the time between each end of a meeting and next start
    #starting from one to avoid the [-inf,-inf] array we added in beginning
    freeTime = []
    for i in range(1, len(meetings)-1):
        freeTime.append([meetings[i][1], meetings[i+1][0]])
    return freeTime

def employee_free_time2(schedule):
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
