from typing import List
import heapq

class MedianFinder:
    min_heap:List[int]
    max_heap:List[int]
    median:float

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.median = 0.0

    def addNum(self, num: int) -> None:
        if num < self.median:
            heapq.heappush(self.min_heap, -num)
            if len(self.min_heap) - len(self.max_heap) == 2:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else :
            heapq.heappush(self.max_heap, num)
            if len(self.max_heap) - len(self.min_heap) == 2:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) == len(self.max_heap):
            self.median = (self.max_heap[0] - self.min_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            self.median = -self.min_heap[0]
        else:
            self.median = self.max_heap[0]


    def findMedian(self) -> float:
        return self.median


def test():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    print( medianFinder.min_heap,medianFinder.max_heap, medianFinder.findMedian())

    medianFinder.addNum(2)
    print( medianFinder.min_heap,medianFinder.max_heap, medianFinder.findMedian())

    medianFinder.addNum(3)
    print( medianFinder.min_heap,medianFinder.max_heap, medianFinder.findMedian())
    medianFinder.addNum(4)
    print( medianFinder.min_heap,medianFinder.max_heap, medianFinder.findMedian())
    medianFinder.addNum(5)
    print( medianFinder.min_heap,medianFinder.max_heap, medianFinder.findMedian())
    medianFinder.addNum(1)
    print( medianFinder.min_heap,medianFinder.max_heap, medianFinder.findMedian())
    medianFinder.addNum(1)
    print( medianFinder.min_heap,medianFinder.max_heap, medianFinder.findMedian())