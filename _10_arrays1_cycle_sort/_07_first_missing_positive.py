#https://leetcode.com/problems/first-missing-positive/submissions/1236584911/
#41. First Missing Positive
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i+1:
                d = nums[i] - 1
                if nums[i] > 0 and nums[i] < len(nums) and nums[d] != nums[i]:
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) +1