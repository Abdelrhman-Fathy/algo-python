#https://leetcode.com/problems/contiguous-array/
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0
        prefixSum = {}
        prefixSum[0] = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                diff -= 1
            else:
                diff += 1
            if diff in prefixSum:
                result = max(result, i + 1 - prefixSum[diff])
            if diff not in prefixSum:
                prefixSum[diff] = i + 1
        return result

        # get target diff and from hashmap
        # store current diff into the hashmap.
