#https://leetcode.com/problems/number-of-islands/

import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # build graph: not needed
        # BFS

        rows = len(grid)
        columns = len(grid[0])
        visited = [[-1 for _ in range(columns)] for _ in range(rows)]

        def getNeighbors(row, column):
            neighbors = []
            if row > 0:
                neighbors.append([row - 1, column])
            if row + 1 < rows:
                neighbors.append([row + 1, column])
            if column > 0:
                neighbors.append([row, column - 1])
            if column +1 < columns:
                neighbors.append([row, column + 1])
            #print(row, column, neighbors)
            return neighbors

        def bfs(row, column):
            #print(visited)
            q = collections.deque([[row, column]])
            visited[row][column] = 1
            while len(q) != 0:
                node = q.popleft()
                for neighbor in getNeighbors(node[0], node[1]):
                    if grid[neighbor[0]][neighbor[1]] == '1' and visited[neighbor[0]][neighbor[1]] == -1:
                        q.append(neighbor)
                        visited[neighbor[0]][neighbor[1]] = 1

        # DFS
        def dfs(row, column):
            visited[row][column] = 1
            for neighbor in getNeighbors(row, column):
                if grid[neighbor[0]][neighbor[1]] == '1' and visited[neighbor[0]][neighbor[1]] == -1:
                    dfs(neighbor[0], neighbor[1])

        # Outerloop
        count = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1' and visited[row][column] == -1:
                    #print(row,column)
                    count += 1
                    #print(grid[row][column], visited[row][column], count)
                    dfs(row, column)
        return count


def test():
    sol = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    #output=1
    #result = sol.numIslands(grid)
    #print(result)
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    # output=3
    #result = sol.numIslands(grid)
    #print(result)

    grid = [["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]]
    # output=1
    result = sol.numIslands(grid)
    print(result)



