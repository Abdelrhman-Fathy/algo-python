#https://leetcode.com/problems/insert-interval/
#57. Insert Interval

def insert(intervals, newInterval):
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
        if result[-1][1] < intervals[i][0]:
            # no overlap
            result.append(intervals[i])
        else:
            # Overlap
            result[-1] = [min(result[-1][0], intervals[i][0]),
                          max(result[-1][1], intervals[i][1])]
    return result

def test():
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    result = insert(intervals, newInterval)
    print(result)
