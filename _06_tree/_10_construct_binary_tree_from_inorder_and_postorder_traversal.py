#106. Construct Binary Tree from Inorder and Postorder Traversal
#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hmap = {}
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        def helper(postOrder, startP, endP, inOrder, startI, endI):
            #base case
            if startP > endP:
                return None
            #recursive case
            rootIndex = hmap[postOrder[endP]]
            node = TreeNode(val=postOrder[endP])
            numRight = endI-rootIndex
            node.left = helper(postOrder, startP, endP-numRight - 1, inOrder, startI, rootIndex - 1)
            node.right = helper(postOrder, endP-numRight, endP-1, inOrder, rootIndex + 1, endI)
            return node
        return helper(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)


