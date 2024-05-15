#https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/1236575979/
#442. Find All Duplicates in an Array

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            while nums[i] != i+ 1:
                d = nums[i] - 1
                if nums[i] != nums[d]:
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result

