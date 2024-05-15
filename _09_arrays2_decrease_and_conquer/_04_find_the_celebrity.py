#https://leetcode.com/problems/find-the-celebrity/description/
#https://leetcode.ca/all/277.html
class Solution:
    def findCelebrity(self, n: int) -> int:
        survivor = 0
        for i in range(1, n):
            if knows(survivor, i):
                survivor = i
        for i in range(n):
            if survivor != i and knows(survivor, i):
                return -1
        return survivor


def knows(a: int, b: int) -> bool:
    graph = [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 1]
    ]
    if graph[a][b] == 1:
        return True
    else:
        return False

def test():
    sol = Solution()
    print(sol.findCelebrity(3))