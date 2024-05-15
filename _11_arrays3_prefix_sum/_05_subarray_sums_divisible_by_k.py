#https://leetcode.com/problems/subarray-sums-divisible-by-k/
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        prefixSum[0] = 1
        runningSum = 0
        result = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            target = (runningSum % k)
            if target in prefixSum:
                result += prefixSum[target]
            mod = target

            if mod in prefixSum:
                prefixSum[mod] += 1
            else:
                prefixSum[mod] = 1

        return result

