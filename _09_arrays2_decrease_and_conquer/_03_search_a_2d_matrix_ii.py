#https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#240. Search a 2D Matrix II

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        row = 0
        col = n - 1
        while col >= 0 and row < m :
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
        return False

def test():
    sol = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    print(sol.searchMatrix(matrix, target))