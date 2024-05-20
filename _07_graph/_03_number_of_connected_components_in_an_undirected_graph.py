#https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
import collections
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #1. build graph
        #2.a bfs
        #2.b dfs
        #3. outer loop

        # 1. build graph
        adjList = [[] for _ in range(n)]
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        visited = [-1] * n

        #2.a bfs
        def bfs(src):
            visited[src] = 1
            q = collections.deque([src])
            while len(q) !=0:
                node = q.popleft()
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        q.append(neighbor)
                        visited[neighbor] = 1

        #2.b dfs
        def dfs(src):
            visited[src] = 1
            for neighbor in adjList[src]:
                if visited[neighbor] == -1:
                    dfs(neighbor)

        components = 0
        for v in range(n):
            if visited[v] == -1:
                components += 1
                bfs(v)
        return components







        pass
def test():
    sol = Solution()
    result = sol.countComponents(5, [[0, 1], [1, 2], [3, 4]])
    print(result)
    result = sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
    print(result)


#Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#Output: 2

#Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#Output:  1