#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/1257765872/
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # intialization
        # get total of first k element
        total = sum(arr[:k])
        result = 0
        # check if total/k >= threshold:
        # increment result
        if total / k >= threshold:
            result += 1

        # for i in k to n-1
        for i in range(k, len(arr)):
            total += arr[i] - arr[i - k]
            # subtract nums[i-k] and add nums[i] to total
            if total / k >= threshold:
                # if average >= threshold:
                result += 1
                # increment result
        return result



