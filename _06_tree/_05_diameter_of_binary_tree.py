#https://leetcode.com/problems/diameter-of-binary-tree/
#543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.global_diameter

    def dfs(self, node):
        # edge case:
        if node is None:
            return 0
        # base case: leaf node
        if node.left is None and node.right is None:
            return 0
        # recursive case: internal node
        myDia = 0
        left = 0
        if node.left is not None:
            left = self.dfs(node.left)
            myDia = left + 1
        right = 0
        if node.right is not None:
            right = self.dfs(node.right)
            myDia += right + 1
        self.global_diameter = max(self.global_diameter, myDia)
        return max(left, right) + 1

