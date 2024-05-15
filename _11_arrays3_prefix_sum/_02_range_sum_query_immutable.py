#https://leetcode.com/problems/range-sum-query-immutable/
from typing import List


class NumArray:
    prefixSum = []

    def __init__(self, nums: List[int]):
        runningSum = 0
        self.prefixSum = []
        for i in range(len(nums)):
            runningSum += nums[i]
            self.prefixSum.append(runningSum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left - 1]

        # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)