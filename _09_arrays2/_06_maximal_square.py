#https://leetcode.com/problems/maximal-square/
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        m = len(matrix)
        table = [[0 for _ in range(n)] for _ in range(m)]
        global_max = 0
        for col in range(n):
            if matrix[0][col] == "1":
                table[0][col] = 1
                global_max = 1
        for row in range(m):
            if matrix[row][0] == "1":
                table[row][0] = 1
                global_max = 1

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == "1":
                    table[row][col] = min(table[row-1][col-1], table[row-1][col], table[row][col-1]) +1
                    global_max = max(table[row][col], global_max)
        print(table)
        print(global_max)
        return global_max * global_max



def test():
    sol = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    print(sol.maximalSquare(matrix))
    matrix = [["0", "1"], ["1", "0"]]

    print(sol.maximalSquare(matrix))
    matrix = [["0"]]
    print(sol.maximalSquare(matrix))
    #print(sol.maximalSquare([6, 6, 5, 6, 3, 8]))


