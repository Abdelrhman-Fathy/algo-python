#https://leetcode.com/problems/subsets-ii/
#90. Subsets II
def subsetsWithDup(nums):
    result = []
    def helper(s, i, slate, result):
        #base case
        if i == len(s):
            result.append(slate[:])
            return
        #recursive case
        #execlude
        helper(s, i+1 , slate, result)

        #include
        slate.append(s[i])
        helper(s, i+1, slate, result)
        slate.pop()

    helper(nums,0,[],result)
    return result
def test():
    nums = [1,2,3]
    result = subsetsWithDup(nums)
    print(result)

