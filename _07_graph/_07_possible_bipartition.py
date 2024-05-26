#https://leetcode.com/problems/possible-bipartition/
from typing import List
import collections

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # build the graph
        graph = [[] for _ in range(n + 1)]
        for (src, dst) in dislikes:
            graph[src].append(dst)
            graph[dst].append(src)

        # BFS
        visited = [-1] * (n + 1)
        levels = [0] * (n + 1)

        def bfs(src):
            q = collections.deque([src])
            visited[src] = 1
            while len(q) != 0:
                node = q.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        q.append(neighbor)
                        visited[neighbor] = 1
                        levels[neighbor] = levels[node] + 1
                    elif levels[neighbor] == levels[node]:
                        return False
            return True

        def dfs(node):
            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    levels[neighbor] = levels[node] + 1
                    if dfs(neighbor) == False:
                        return False
                elif (levels[neighbor] - levels[node]) % 2 == 0:
                    return False
            return True

        # outer loop
        for v in range(1, n + 1):
            if visited[v] == -1:
                if dfs(v) == False:
                    return False
        return True


