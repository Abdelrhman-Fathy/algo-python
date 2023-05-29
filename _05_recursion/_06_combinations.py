#https://leetcode.com/problems/combinations/
#77. Combinations
#backtracking
def combine(n,k):
    result = []
    nums = [x for x in range(1,n+1)]
    helper(nums,k,0,[],result)
    return result
def helper(s,k, i, slate, result):
    #backtrack case
    if len(slate) == k:
        result.append(slate[:])
        return
    #base case
    if i == len(s):
        return
    #recursive case
    #execlude
    helper(s,k, i+1 , slate, result)

    #include
    slate.append(s[i])
    helper(s,k, i+1, slate, result)
    slate.pop()
def test():
    n = 4
    k = 2
    result = combine(n,k)
    print(result)

