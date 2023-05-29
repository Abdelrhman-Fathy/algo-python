#https://leetcode.com/problems/permutations/
#46. Permutations

def permute(nums):
    result = []
    def helper(s, i, slate):
        if i == len(s):
            result.append(slate[:])
            return
        for pick in range(i, len(s)):
            s[i],s[pick] = s[pick], s[i]
            slate.append(s[i])
            helper(s, i+1, slate)
            slate.pop()
            s[i],s[pick] = s[pick], s[i]

    helper(nums,0,[])
    return result

def test():
    nums = [1,2,3,4,5,6,7,8,9,10]
    result = permute(nums)
    print(result)