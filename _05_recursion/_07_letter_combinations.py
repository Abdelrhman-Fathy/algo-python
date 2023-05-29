#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#17. Letter Combinations of a Phone Number
def letterCombinations(digits):
    letters = {'2':['a','b','c'],'3':['d','e','f'],
               '4':['g','h','i'],'5':['j','k','l'],
               '6': ['m', 'n', 'o'],'7': ['p', 'q', 'r', 's'],
               '8':['t','u','v'],'9':['w','x','y','z']}
    result = []
    helper(digits,letters,0,[],result)
    return result
def helper(s,letters,i,slate,result):
    if i == len(s):
        if len(slate) > 0:
            result.append(''.join(slate))
        return
    for c in letters.get(s[i]):
        slate.append(c)
        helper(s,letters, i+1, slate, result)
        slate.pop()

def test():
    #digits = "23"
    digits = ""
    result = letterCombinations(digits)
    print(result)