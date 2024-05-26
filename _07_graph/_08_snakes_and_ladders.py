#https://leetcode.com/problems/snakes-and-ladders/
import collections
from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # board[r][c] != -1 snake or ladder, new destination is board[r][c]

        # build graph------->
        # build jump array
        # loop on the board from down to top
        # for each row, if row number is even insert it into jump array
        # insert one row forward and other row backward

        jump = [-1]
        forward = True
        for row in range(len(board) - 1, -1, -1):
            if forward:
                jump += board[row][:]
            else:
                jump += board[row][::-1]
            forward = not forward
        #print(jump)

        #get neighbors
        size = len(board) * len(board[0])
        def getNeighbors(current):
            neighbors = []
            #print("limit:", min(current + 7, size+1))
            for i in range(current + 1, min(current + 7, size+1)):
                neighbor =  i
                if jump[neighbor] != -1:
                    neighbor = jump[neighbor]
                neighbors.append(neighbor)
            return neighbors

        # bfs
        visited = [-1] * (size + 1)
        distance = [-1] * (size + 1)
        def bfs(src):
            q = collections.deque([src])
            visited[src] = 1
            distance[src] = 0
            while len(q) != 0:
                node = q.popleft()
                neighbors = getNeighbors(node)
                #print("node:", node, " ,neighbors:", neighbors)
                for neighbor in neighbors:
                    if visited[neighbor] == -1:
                        q.append(neighbor)
                        visited[neighbor] = 1
                        distance[neighbor] = distance[node] + 1
        # outter loop start from square 1
        bfs(1)
        return distance[size]

        # row is odd 1,0 = 2n till 1,n = n+1
        # row is even 0,0 = 1 til 0,n = n

        # Intialize array with lenght of n**2 + 1


def test():
    """
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    sol = Solution()
    result = sol.snakesAndLadders(board)
    print(result)

    board = [[-1,-1],[-1,3]]
    sol = Solution()
    result = sol.snakesAndLadders(board)
    print(result)

    board = [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]
    sol = Solution()
    result = sol.snakesAndLadders(board)
    print(result)

        board = [[-1, -1, -1, -1, 15],
             [25, -1, 20, -1, -1],

             [-1, 17, -1, 19, -1],
             [2,-1,-1,6,-1],
             [-1,-1,19,10,-1],]

    [-1,
     -1, -1, -1, -1, 15,
     25, -1, 20, -1, -1,
     -1, 17, -1, 19, -1,
     2, -1, -1, 6, -1,
     -1, -1, 19, 10, -1]
"""
    board = [[-1,-1,19,10,-1],
             [2,-1,-1,6,-1],
             [-1,17,-1,19,-1],
             [25,-1,20,-1,-1],
             [-1,-1,-1,-1,15]]


    sol = Solution()
    result = sol.snakesAndLadders(board)
    print(result)



#Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
#Output: 4

#Input: board = [[-1,-1],[-1,3]]
#Output: 1