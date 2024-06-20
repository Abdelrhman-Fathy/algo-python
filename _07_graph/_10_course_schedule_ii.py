#https://leetcode.com/problems/course-schedule-ii/
from typing import List
class Solution:
    time = 0

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the graph
        graph = [[] for _ in range(numCourses)]
        for (course, prereq) in prerequisites:
            graph[prereq].append(course)

        # dfs
        visited = [-1] * numCourses
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        result = []

        def dfs(node):
            visited[node] = 1
            arrival[node] = self.time
            self.time += 1
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    if dfs(neighbor) == True:
                        return True
                elif departure[neighbor] == -1:
                    return True
            departure[node] = self.time
            result.append(node)
            self.time += 1
            return False

        # outter loop
        for vertex in range(numCourses):
            if visited[vertex] == -1:
                if dfs(vertex) == True:
                    return []
        return result[::-1]

def test():
    sol = Solution()

    numCourses = 2
    prerequisites = [[1,0]]
    result = sol.findOrder(numCourses, prerequisites)
    print(result)
    #Output:[0,1]

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    result = sol.findOrder(numCourses, prerequisites)
    print(result)
    #Output:[0,2,1,3]

    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    result = sol.findOrder(numCourses, prerequisites)
    print(result)
    # Output:[]



