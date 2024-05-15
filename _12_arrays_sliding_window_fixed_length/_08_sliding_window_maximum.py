#https://leetcode.com/problems/sliding-window-maximum/
import collections
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # intialize
        deq = collections.deque()

        def pushin(val):
            while deq and val > deq[-1]:
                deq.pop()
            deq.append(val)

        for i in range(k):
            pushin(nums[i])
        result = [deq[0]]

        for i in range(k, len(nums)):
            if nums[i - k] == deq[0]:
                deq.popleft()
            pushin(nums[i])
            result.append(deq[0])
        return result


