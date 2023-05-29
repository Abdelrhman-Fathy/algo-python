def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if result[-1][1] < intervals[i][0]:
            #no overlap
            result.append(intervals[i])
        else:
            #Overlap
            result[-1] = [result [-1][0], max(result[-1][1], intervals[i][1])]
    return result


def test():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge(intervals)
    print(result)