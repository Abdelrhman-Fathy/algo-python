#https://leetcode.com/problems/graph-valid-tree/description/
#261. Graph Valid Tree
import collections
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Analysis: one component and no cycles
        #build graph
        #bfs/dfs
        #outer loop

        #build graph
        adjList = [[] for _ in range(n)]
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        visited = [-1] * n
        parent = [-1] * n
        #bfs
        def bfs(src):
            q = collections.deque([src])
            visited[src] = 1
            while len(q) != 0:
                node = q.popleft()
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:

                        visited[neighbor] = 1
                        parent[neighbor] = node
                        q.append(neighbor)

                    else: #cycle detected
                        if parent[node] != neighbor:
                            return True
            return False

        def dfs(src):
            visited[src] = 1
            for neighbor in adjList[src]:
                if visited[neighbor] == -1:
                    parent[neighbor] = src
                    if dfs(neighbor):
                        return True
                else:
                    if parent[src] != neighbor:
                        return True
            return False

        #outer loop
        count = 0
        for v in range(n):
            if visited[v] == -1:
                count +=1
                if dfs(v):
                    return False
            if count>1:
                return False

        return True




def test():
    sol = Solution()
    n = 5
    edges = [[0,1], [0,2], [0,3], [1,4]]
    result = sol.validTree(n, edges)
    print(result)

    n = 5
    edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    result = sol.validTree(n, edges)
    print(result)

#Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
#Output: true


#Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
#Output: false