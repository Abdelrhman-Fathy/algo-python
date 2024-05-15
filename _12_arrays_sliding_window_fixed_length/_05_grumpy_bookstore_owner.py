#https://leetcode.com/problems/grumpy-bookstore-owner/submissions/1257815676/
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        total = sum(customers[:minutes])
        for i in range(minutes, len(customers)):
            if grumpy[i] == 0:
                total += customers[i]

        gmax = total
        for i in range(minutes, len(customers)):
            removed = 0
            if grumpy[i-minutes] == 1:
                removed = customers[i-minutes]
            added = 0
            if grumpy[i] == 1:
                added = customers[i]
            total += added-removed
            gmax = max(gmax, total)
        return gmax