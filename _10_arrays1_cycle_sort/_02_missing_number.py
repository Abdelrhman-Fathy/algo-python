#leetcode 268
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                d = nums[i]
                if d < len(nums):
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
