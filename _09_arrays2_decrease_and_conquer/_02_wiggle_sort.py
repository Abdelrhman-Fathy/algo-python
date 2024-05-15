from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            if i%2 == 0 and nums[i] > nums[i-1] : #even
                nums[i], nums[i-1] = nums[i-1], nums[i]
            if i%2==1 and nums[i] < nums[i-1] : #odd
                nums[i], nums[i-1] = nums[i-1], nums[i]


        return nums

def test():
    sol = Solution()
    print(sol.wiggleSort([3,5,2,1,6,4]))
    print(sol.wiggleSort([6, 6, 5, 6, 3, 8]))





#Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#Input: nums = [3,5,2,1,6,4]
#Output: [3,5,1,6,2,4]
#Explanation: [1,6,2,5,3,4] is also accepted.

#Input: nums = [6,6,5,6,3,8]
#Output: [6,6,5,6,3,8]