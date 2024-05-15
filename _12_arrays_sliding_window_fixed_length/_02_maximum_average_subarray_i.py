#https://leetcode.com/problems/maximum-average-subarray-i/
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # intialization case
        # get the sum for first k elements
        total = sum(nums[:k])
        # gmax = total/k
        gmax = total /k

        # other case
        # for i in k to n-1:
        for i in range(k, len(nums)):
            total += nums[i] - nums[ i -k]
            # add nums[i] to total
            # subtract nums[i-k] from total
            # average = total/k
            average = total /k
            # gmax = max(gmax, average)
            gmax = max(gmax ,average)
        return gmax

