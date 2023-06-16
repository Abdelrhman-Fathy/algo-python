import heapq
from typing import List


class KthLargest:
    nums: List[int]
    k: int

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        #print(self.nums)
        return self.nums[0]


def test():
    test = KthLargest(3, [4, 5, 8, 2])

    print(test.nums,test.add(3))
    print(test.nums,test.add(5))
    print(test.nums,test.add(10))
    print(test.nums,test.add(9))
    print(test.nums,test.add(4))
