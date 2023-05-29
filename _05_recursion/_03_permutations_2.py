#https://leetcode.com/problems/permutations-ii/
#47. Permutations II

def permuteUnique(nums):
    result = []

    def helper(s, i, slate, result):
        if i ==len(s):
            result.append(slate[:])
            return
        seen = set()
        for pick in range(i, len(s)):
            if s[pick] in seen:
                continue
            seen.add(s[pick])
            s[i], s[pick] = s[pick], s[i]
            slate.append(s[i])
            helper(s, i+1, slate, result)
            slate.pop()
            s[i], s[pick] = s[pick], s[i]

    helper(nums, 0, [], result)
    return result


def test():
    #nums = [1,1,2]
    nums = [1, 2, 3]
    result = permuteUnique(nums)
    print(result)