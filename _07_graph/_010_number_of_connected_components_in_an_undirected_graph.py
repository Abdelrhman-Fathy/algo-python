from typing import List
from queue import Queue


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for x in range(n)]
        visited = [-1 for x in range(n)]
        print(adjList)
        #1. Time: O(m)
        # space of adj list O(n) for the nodes and O(2m) for the neighbors, = O(m+n)
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)  # valid for undirected graph only
        print(adjList)
        #BFS Time : O(m+n)
        ##2. Time: O(N) push and pop all vertices and O(m) for visiting neighbors of each node
        #aux space of queue size: O(n) if one node has eadges with all other node
        def bfs(source):
            q = Queue()
            visited[source] = 1
            q.put(source)

            #2. Time: Sum[ O(Degree(v))] hence we are visiting the neighbors of each node
            # since each edge will be visited twice, once from each side (vertix) hence O(Degree(V)) = 2m = O(m)
            while not q.empty():
                node = q.get()
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        q.put(neighbor)

        #3. time:O(n+m)
        # O(N) pushing the vertix to the call stack by calling dfs function
        # and at the end of the function pulling the call from call stack across all the nodes
        #O(m) because we are visiting the neighbors of each node m is number of edges and we are visiting each edge twice once from each vertix
        #Aux space: O(n) the maximum size if the stack is the height of the tree which is at maximum from root to leaf could be of size n
        


        def dfs(source):
            #test
            visited[source] = 1
            for neighbor in adjList[source]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    dfs(neighbor)

        ##4. Time: O(N)##
        components = 0
        for v in range(n):
            if visited[v] == -1:
                components += 1
                #bfs(v)
                dfs(v)
        return components


def test():
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    #n = 5
    #edges = [[0, 1], [1, 2], [3, 4]]
    sol = Solution()
    print(sol.countComponents(n, edges))
