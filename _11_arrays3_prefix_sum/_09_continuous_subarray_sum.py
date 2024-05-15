#https://leetcode.com/problems/continuous-subarray-sum/
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = {}
        prefixSum[0] = 0
        mod = 0
        for i in range(len(nums)):
            mod = (mod + nums[i])%k
            target = mod
            print(prefixSum)
            if target in prefixSum:
                length = i+1 - prefixSum[target]
                if length>1:
                    return True
            if mod not in prefixSum:
                prefixSum[mod] = i+1
        return False

def test():
    sol = Solution()
    nums = [23,2,4,6,7]
    k = 6
    result = sol.checkSubarraySum(nums,k)
    print(result)