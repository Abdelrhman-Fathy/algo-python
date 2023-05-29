#https://leetcode.com/problems/path-sum-ii/submissions/
#113. Path Sum II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import List
class Solution:
    result: List
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        self.dfs(root, targetSum, [])
        return self.result

    def dfs(self, node, targetSum, slate):
        # edge case
        if node is None:
            return
        # base case : leaf node
        if node.left is None and node.right is None:
            if targetSum == node.val:
                slate.append(node.val)
                self.result.append(slate[:])
                slate.pop()
            return
        # recursive case: internal node
        if node.left is not None:
            slate.append(node.val)
            self.dfs(node.left, targetSum - node.val, slate)
            slate.pop()
        if node.right is not None:
            slate.append(node.val)
            self.dfs(node.right, targetSum - node.val, slate)
            slate.pop()
