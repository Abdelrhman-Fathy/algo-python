#https://leetcode.com/problems/letter-case-permutation/
#784. Letter Case Permutation

def letterCasePermutation(s):
    result = []

    def helper(s, i, slate):
        #base case
        if i == len(s):
            result.append(''.join(slate))
            return
        #recursion case
        if s[i].isalpha():
            slate.append(s[i].lower())
            helper(s, i + 1, slate)
            slate.pop()
            slate.append(s[i].upper())
            helper(s, i + 1, slate)
            slate.pop()
        else:
            slate.append(s[i])
            helper(s, i + 1, slate)
            slate.pop()
    helper(s, 0, [])
    return result


def test():
    #s = "a1b2"
    s = "a1b2a1b2a1b2a1b2a1b2a1b2a1b2a1b2a1b2a1b2a1b2a1b2a1b2"
    result = letterCasePermutation(s)
    print(result)
    # Output = ["a1b2", "a1B2", "A1b2", "A1B2"]
