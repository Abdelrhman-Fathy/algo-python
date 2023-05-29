#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    hmap: dict
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hmap = {}
        for i in range(len(inorder)):
            self.hmap[inorder[i]] = i
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, P, startP, endP, I, startI, endI):
        # base case
        if startP > endP:
            return None
        if startP == endP:
            return TreeNode(val=P[startP])

        # recursive case
        rootNode = TreeNode(val=P[startP])
        rootIndex = self.hmap[P[startP]]
        numLeft = rootIndex - startI
        numRight = endI - rootIndex
        #print(startP + numLeft, rootIndex)
        #print(startP + numLeft + 1, rootIndex + 1)
        rootNode.left = self.helper(P, startP + 1, startP + numLeft,
                                    I, startI, rootIndex - 1)
        rootNode.right = self.helper(P, startP + numLeft + 1, endP,
                                     I, rootIndex + 1, endI)
        return rootNode
#T(n):O(n)
#S(n):Implicit call stack: O(n) + explicit O(n) Tree + O(n) hashmap = O(n)
#leetcode 1008, 106
