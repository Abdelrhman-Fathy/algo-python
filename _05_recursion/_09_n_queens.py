#https://leetcode.com/problems/n-queens/
#51. N-Queens
result = []
def solveNQueens(n):
    helper(0, n, [])
    return result

#slate will be storing the column of the placed queens.
# we have N queens, one in each row. each queen can be placed in N columns.
#O(N^N)
def helper(i, n, slate): # each queen placed at a row i, and column slate[i
    #print(slate)
    #backtracking case
    lastQ = len(slate) - 1
    for earlierQ in range(lastQ):
        if slate[earlierQ] == slate[lastQ]: #column conflect
            return
        rowDiff = abs(lastQ-earlierQ)
        colDiff = abs(slate[lastQ] - slate[earlierQ])
        if rowDiff == colDiff:
            return
    #base case
    if i == n :
        result.append(slate[:])
        return

    #recursive case
    for col in range(n):
        slate.append(col)
        helper(i+1, n, slate)
        slate.pop()




def test():
    print("nQueens1",solveNQueens(6))
