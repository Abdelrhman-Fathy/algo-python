#https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum = {}
        prefixSum["even"] = 1
        prefixSum["odd"] = 0

        runningSum = 0
        result = 0

        for i in range(len(arr)):
            runningSum += arr[i]
            if runningSum % 2 == 0:  # even
                result += prefixSum["odd"]
            else:
                result += prefixSum["even"]
            if runningSum % 2 == 0:
                prefixSum["even"] += 1
            else:
                prefixSum["odd"] += 1
            result = result % (10 ** 9 + 7)
        return result





