#https://leetcode.com/problems/subarray-sum-equals-k
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        prefixSum[0] = 1
        runningSum = 0
        result = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            target = runningSum - k
            if target in prefixSum:
                result += prefixSum[target]

            if runningSum in prefixSum:
                prefixSum[runningSum] += 1
            else:
                prefixSum[runningSum] = 1
        return result