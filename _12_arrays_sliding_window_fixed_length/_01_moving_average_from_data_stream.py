#https://leetcode.com/problems/moving-average-from-data-stream/description/
import collections


class MovingAverage:

    def __init__(self, size: int):
        self.maxSize = size
        self.window = collections.deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.total += val
        if self.maxSize < len(self.window):
            popped = self.window.popleft()
            self.total -= popped
        return float(self.total/len(self.window))


def test():
    MovingAverage
    m = MovingAverage(3)
    result = m.next(1)
    print(result)
    result = m.next(10)
    print(result)
    result = m.next(3)
    print(result)
    result = m.next(5)
    print(result)