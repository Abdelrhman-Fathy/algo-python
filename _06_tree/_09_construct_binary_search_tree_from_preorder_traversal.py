# Definition for a binary tree node.
#https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
#1008. Construct Binary Search Tree from Preorder Traversal

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import List, Optional
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        hmap = {}
        inOrder = preorder[:]
        inOrder.sort()
        for i in range(len(inOrder)):
            hmap[inOrder[i]] = i
        def helper(preOrder,startP, endP, inOrder, startI, endI):
            if startP > endP:
                return None
            rootIndex = hmap[preOrder[startP]]
            numLeft = rootIndex - startI
            root = TreeNode(val=preOrder[startP])
            root.left = helper(preOrder, startP+1, startP+numLeft,
                               inOrder, startI, rootIndex - 1)
            root.right = helper(preOrder, startP+numLeft + 1, endP,
                                inOrder, rootIndex + 1, endI)
            return root
        return helper(preorder, 0, len(preorder) - 1, inOrder, 0, len(inOrder) - 1)


