#https://leetcode.com/problems/diet-plan-performance/description/
from typing import List

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        #Intialize
        result = 0
        total = sum(calories[:k])
        if total < lower:
            result -= 1
        elif total > upper:
            result += 1

        for i in range(k, len(calories)):
            total += calories[i] - calories[i-k]
            if total < lower:
                result -= 1
            elif total > upper:
                result += 1
        return result



def test():
    sol = Solution()

    calories = [1,2,3,4,5]; k = 1; lower = 3; upper = 3

    result = sol.dietPlanPerformance(calories, k, lower, upper)
    print(result)
    #Output: 0


    calories = [3,2]; k = 2; lower = 0; upper = 1
    result = sol.dietPlanPerformance(calories, k, lower, upper)
    print(result)
    #Output: 1
