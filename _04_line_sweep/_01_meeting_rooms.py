#https://leetcode.com/problems/meeting-rooms/

def meeting_rooms(a):
    a.sort(key=lambda x: x[0])
    next_start: int
    for i in range(len(a)):
        if i == len(a) - 1:
            next_start = float('INF')
        else:
            next_start = a[i + 1][0]
        if a[i][1] > next_start:
            return False
    return True


def meeting_rooms2(a):
    a.sort(key=lambda x: x[0])
    for meeting in range(len(a) - 1):
        if a[meeting][1] > a[meeting + 1][0]:
            return False
    return True


def test():
    a = [[5, 10], [30, 40], [0, 5], [15, 31]]
    print(meeting_rooms(a))
