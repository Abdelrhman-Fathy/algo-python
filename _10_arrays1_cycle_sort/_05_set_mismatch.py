#645. Set Mismatch
#https://leetcode.com/problems/set-mismatch/
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                d = nums[i] - 1
                if nums[d] != nums[i]:
                    nums[d], nums[i] = nums[i], nums[d]
                else:
                    break
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        return []
