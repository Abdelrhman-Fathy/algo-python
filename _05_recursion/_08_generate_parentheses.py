#https://leetcode.com/problems/generate-parentheses/
#22. Generate Parentheses

def generateParenthesis(n):
    result = []
    helper(n,n, [], result)
    return result


def helper(numleft, numright, slate, result):
    # backtrack case
    if numleft > numright:
        return
    # base case:
    if numleft == 0 and numright == 0:
        result.append("".join(slate))
    # recursive case
    # add (
    if numleft > 0:
        slate.append('(')
        helper(numleft - 1, numright, slate, result)
        slate.pop()
    # add )
    if numright > 0:
        slate.append(')')
        helper(numleft, numright - 1, slate, result)
        slate.pop()

def test():
    result = generateParenthesis(4)
    print(result)

