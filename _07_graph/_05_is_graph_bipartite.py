#https://leetcode.com/problems/is-graph-bipartite/
import collections
from typing import List
"""
graph is bipartite in 2 cases
    1. it is a tree without cycles
    2. Any of its components has a cycle with an odd number of nodes
        1. BFS: cycle with an odd number nodes can be detected if
            1. it has cross edge (visited node except parent) cycle detected.
            2. The cross edge connecting 2 nodes in the same layer, not adjacent layers. : odd number of nodes detected.
        2. DFS: cycle with an odd number of nodes can be detected by the following
            1. it has back edge, means there is a visited node that is not the parent: cycle detected
            2. the backed connecting a node that has a color similar to my color, means depth difference is even
            
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        #build the graph: already built
        n = len(graph)
        #BFS

        visited = [-1] * n
        level = [-1] * n
        def bfs(src):
            q = collections.deque([src])
            visited[src] = 1
            level[src] = 0
            while len(q) != 0:
                node = q.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        q.append(neighbor)
                        visited[neighbor] = 1
                        level[neighbor] = level[node] + 1
                    else:
                        if level[neighbor] == level[node]:
                            return False
            return True
        def dfs(node):
            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    level[neighbor] = level[node] + 1
                    if not dfs(neighbor):
                        return False
                else:
                    if (level[neighbor] - level[node])%2 == 0:
                        return False
            return True

        #DFS
        #outer loop
        for v in range(len(graph)):
            if visited[v] == -1:
                if bfs(v) == False:
                    return False
        return True