#40. Combination Sum II
#https://leetcode.com/problems/combination-sum-ii/
result = []
target:int
def combinationSum2(candidates, target):
    candidates.sort()
    helper(candidates, 0, [], 0, target)
    return result
def helper(s, i, slate, slate_sum, target):
    #backtracking case
    if slate_sum > target:
        return

    #base case
    if i == len(s):
        if slate_sum == target:
            print(slate, slate_sum, slate_sum > target)
            result.append(slate[:])
        return

    #recursive case

    #execlude
    count = 0
    for index in range(i, len(s)):
        if s[index] != s[i]:
            break
        count += 1
    helper(s, i+count, slate, slate_sum, target)

    #include
    for c in range(count):
        slate.append(s[i])
        helper(s, i + count, slate, slate_sum + s[i]*(c+1), target)
    for c in range(count):
        slate.pop()

def test():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    #candidates = [1,1,2,5,6,7,10,0,0]
    #candidates = [1,2,1,6]
    target = 8
    print(combinationSum2(candidates, target))