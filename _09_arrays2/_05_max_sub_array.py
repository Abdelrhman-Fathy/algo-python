from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        g = nums[0]
        f= nums[0]
        for i in range(1, len(nums)):
            f = max(nums[i], f + nums[i])
            g = max(g, f)
        return g