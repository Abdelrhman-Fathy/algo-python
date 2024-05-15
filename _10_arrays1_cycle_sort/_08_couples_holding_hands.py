from typing import List
#https://leetcode.com/problems/couples-holding-hands/submissions/1236926228/
#765. Couples Holding Hands
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # load numbers in a map
        indices = {}
        for i in range(len(row)):
            indices[row[i]] = i
        sofas = len(row) // 2
        swaps = 0
        # loop on each sofa.
        for i in range(sofas):
            # keep the left seat in its place
            rightSeat = (i+1) * 2 - 1
            leftSeat = (i+1) * 2 - 2
            # find the expected values of right seat
            expectedRight = self.getExpectedRight(row, leftSeat)
            # while right Seat not its place
            while row[rightSeat] != expectedRight:
                destination = self.getDestination(row[rightSeat], indices)
                # swap the distination index into its correct place
                row[rightSeat], row[destination] = row[destination], row[rightSeat]
                # update the map with the new places of the swapped numbers
                indices[row[rightSeat]] = rightSeat
                indices[row[destination]] = destination
                # increment swap
                swaps += 1
        # return number of swaps
        return swaps

    def getExpectedRight(self, row, leftSeat):
        if row[leftSeat] % 2 == 0:  # even
            return row[leftSeat] + 1
        else:
            return row[leftSeat] - 1

    def getDestination(self, rightElm, indices):
        # find the proper neighbor
        if rightElm % 2 == 0:  # even
            neighbor = rightElm + 1
        else:
            neighbor = rightElm - 1
        # get neighbor index
        neighborIndex = indices[neighbor]
        # get the distnation index
        if neighborIndex % 2 == 0:  # even
            index = neighborIndex + 1
        else:
            index = neighborIndex - 1
        # return destination index
        return index

def test():
    sol = Solution()
    row = [0,2,1,3]
    row = [3,2,0,1]
    print(sol.minSwapsCouples(row))
