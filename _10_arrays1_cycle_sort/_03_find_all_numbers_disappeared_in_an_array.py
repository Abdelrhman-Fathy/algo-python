#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
#448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # nums = [1,2,1]
        result = []
        for i in range(len(nums)):
            while nums[i] != i+ 1:
                d = nums[i] - 1
                if nums[d] != nums[i]:
                    nums[d], nums[i] = nums[i], nums[d]
                else:
                    break
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result


