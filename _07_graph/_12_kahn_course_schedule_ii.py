#https://leetcode.com/problems/course-schedule-ii/
import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the graph
        graph = [[] for _ in range(numCourses)]
        for (course, prereq) in prerequisites:
            graph[prereq].append(course)
        def kahn():
            # build inDegree array
            inDegree = [0] * numCourses
            for node in range(numCourses):
                for neighbor in graph[node]:
                    inDegree[neighbor] += 1

            #find the sources and put in bag
            bag = collections.deque()
            for node in range(numCourses):
                if inDegree[node] == 0 :
                    bag.append(node)
            topSort = []
            #while bag is not empty
            while len(bag) != 0:
                node = bag.popleft()
                #add node to topSort
                topSort.append(node)
                #get neighbors
                for neighbor in graph[node]:
                    # reduce neighbors in Degree by 1
                    inDegree[neighbor] -= 1
                    # if neighbor inDegree is 0 add it to the bag
                    if inDegree[neighbor] == 0 :
                        bag.append(neighbor)
            #loop on the visited array, if any node not visited, there is a cycle
            if len(topSort) != numCourses:
                return []
            return topSort
        return kahn()

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
    #correct Output:[0,2,1,3] actual output: [0, 1, 2, 3]

    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    result = sol.findOrder(numCourses, prerequisites)
    print(result)
    # Output:[]
