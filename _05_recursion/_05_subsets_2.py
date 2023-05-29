# https://leetcode.com/problems/subsets-ii/
# 90. Subsets II
def subsetsWithDup(nums):
    result = []
    nums.sort()
    helper(nums, 0, [], result)
    return result


def helper(s, i, slate, result):
    # base case
    if i == len(s):
        result.append(slate[:])
        return
    # recursive case
    count = 0
    for index in range(i, len(s)):
        if s[index] != s[i]:
            break
        count += 1
    # exclude
    helper(s, i + count, slate, result)
    # include
    for c in range(count):
        slate.append(s[i])
        helper(s, i + count, slate, result)
    for c in range(count):
        slate.pop()


def test():
    nums = [1, 2, 2]
    result = subsetsWithDup(nums)
    print(result)
