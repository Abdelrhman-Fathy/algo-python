#https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
from typing import List
#Input: nums = [1, -1, 5, -2, 3], k = 3
#Output: 4

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        prefixSum[0] = 0
        runningSum = 0
        result = 0

        runningSumd = []
        targetd = []
        resultd = []
        for i in range(len(nums)):
            runningSum += nums[i]
            target = runningSum - k
            runningSumd.append(runningSum)
            targetd.append(target)
           #print("target:", target,", prefixSum:",prefixSum)
            if target in prefixSum:
                result = max(result, i +1 - prefixSum[target])

            if runningSum not in prefixSum:
                prefixSum[runningSum] = i+1
            resultd.append(result)
        return result

def test():
    sol = Solution()
    nums = [1, -1, 5, -2, 3]
    k = 3
    result = sol.maxSubArrayLen(nums,k)
    print(result) #4

    nums = [-2, -1, 2, 1]
    k = 1
    #result = sol.maxSubArrayLen(nums, k)
    #print(result) #Output: 2



