#https://leetcode.com/problems/n-queens/
#51. N-Queens
def solveNQueens(n):
    s = [i for i in range(n)]
    result = []
    def helper(i, n, slate): # each queen placed at a row i, and column slate[i
        #backtracking case
        lastQ = len(slate) - 1
        for earlierQ in range(lastQ):
            rowDiff = abs(lastQ-earlierQ)
            colDiff = abs(slate[lastQ] - slate[earlierQ])
            if rowDiff == colDiff:
                return
        #base case
        if i == n:
            row = []
            for i in range(len(slate)):
                row.append("."*slate[i]+"Q"+"."*(n-slate[i]-1))
            result.append(row)
            return
        #recursive case
        for pick in range(i, len(s)):
            s[i], s[pick] = s[pick], s[i]
            slate.append(s[i])
            helper(i+1, n, slate)
            slate.pop()
            s[i],s[pick] = s[pick], s[i]

    helper(0, n, [])
    return result

def test():
    n = 4
    result = solveNQueens(n)
    print("nQueens2",result)
    #nQueens2 [[1, 3, 0, 2], [2, 0, 3, 1]]



#slate will be storing the column of the placed queens.
# we have N queens, one in each row. each queen can be placed in N columns.
#O(N^N)

