#https://leetcode.com/problems/range-sum-query-2d-immutable/
from typing import List

class NumMatrix:
    prefixSum = []

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        n = len(matrix[0])
        m = len(matrix)
        self.prefixSum = [[0 for _ in range(n)] for _ in range(m)]
        runningSum = 0
        for i in range(len(matrix)):
            runningSum += matrix[i][0]
            self.prefixSum[i][0] = runningSum
        runningSum = 0
        for i in range(len(matrix[0])):
            runningSum += matrix[0][i]
            self.prefixSum[0][i] = runningSum

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefixSum[i][j] = matrix[i][j] + self.prefixSum[i - 1][j] + self.prefixSum[i][j - 1] - \
                                       self.prefixSum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefixSum[row2][col2]
        elif row1 == 0:
            return self.prefixSum[row2][col2] - self.prefixSum[row2][col1 - 1]
        elif col1 == 0:
            return self.prefixSum[row2][col2] - self.prefixSum[row1 - 1][col2]
        else:
            return self.prefixSum[row2][col2] - self.prefixSum[row1 - 1][col2] - self.prefixSum[row2][col1 - 1] + \
                   self.prefixSum[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)