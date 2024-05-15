#287. Find the Duplicate Number
#https://leetcode.com/problems/find-the-duplicate-number/description/
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i+1:
                d = nums[i] - 1
                if nums[i] != nums[d]:
                    nums[d], nums[i] = nums[i], nums[d]
                else:
                    break
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]
        return -1