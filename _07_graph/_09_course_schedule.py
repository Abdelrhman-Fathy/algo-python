#https://leetcode.com/problems/course-schedule/
import collections
from typing import List

class Solution:
    time = 0
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build the graph
        graph = [[] for _ in range(numCourses)]
        for (prereq, course) in prerequisites:
            graph[course].append(prereq)
        visited = [-1] * numCourses
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        self.time = 0
        def dfs(node):
            visited[node] = 1
            arrival[node] = self.time
            self.time += 1
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    if dfs(neighbor) == True:
                        return True
                else:
                    if departure[neighbor] == -1: #cycle detected
                        return True
            departure[node] = self.time
            self.time += 1
            return


        #kahn algorithm
        def kahn():
            #calculate the in degree
            inDegree = [0] * numCourses
            for node in range(numCourses):
                for neighbor in graph[node]:
                    inDegree[neighbor] += 1
            #look for the nodes with zero in degree to start with
            deq = collections.deque()
            for node in range(numCourses):
                if inDegree[node] == 0 and visited[node] == -1:
                    deq.append(node)
                    visited[node] = 1
            while len(deq) != 0:
                node = deq.popLeft()
                for neighbor in graph[node]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0 and visited[neighbor] == -1:
                        deq.append(neighbor)
                        visited[neighbor] = 1
            for node in range(numCourses):
                if visited[node] == -1:
                    return True



        #outer loop
        for node in range(numCourses):
            if visited[node] == -1:
                if dfs(node) == True:
                    return False
        return True
def test():
    sol = Solution()

    numCourses = 2
    prerequisites = [[1,0]]
    result = sol.canFinish(numCourses, prerequisites)
    print(result)
    #true

    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    result = sol.canFinish(numCourses, prerequisites)
    print(result)
    #Output: false