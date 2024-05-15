from typing import List
class Solution:
    def cycleSort(self, nums: List[int]) -> None:
        print(self.rank(nums, nums[3]))
        for i in range(len(nums)):
            while i != self.rank(nums, nums[i]) - 1:
                rank = self.rank(nums, nums[i])
                nums[i], nums[rank - 1] = nums[rank - 1], nums[i]


    def rank(self, nums:List[int], currentNumber:int) -> int:
        rank = 0
        for i in range(len(nums)):
            if nums[i] < currentNumber:
                rank += 1
        return rank + 1
def test():
    sol = Solution()
    nums = [17, 19, 13, 7, 1, 5, 15, 11, 9, 3, 21]
    sol.cycleSort(nums)
    print(nums)
