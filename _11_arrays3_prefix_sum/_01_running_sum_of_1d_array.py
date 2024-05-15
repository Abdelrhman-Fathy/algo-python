#https://leetcode.com/problems/running-sum-of-1d-array/description/
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i - 1] + nums[i])
        return prefixSum
