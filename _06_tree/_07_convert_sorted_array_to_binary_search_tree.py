#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#108. Convert Sorted Array to Binary Search Tree

#T(n) = O(n)
#S(n) = O(log n) implicit stack space + explicit space for output is O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums is None:
            return None
        return self.helper(nums, 0, len(nums) - 1)
        self.helper()

    def helper(self, nums, start, end):
        # base case:
        if start > end:
            return None
        # recursive case: internal node
        mid = start + (end - start) // 2
        node = TreeNode(val=nums[mid])
        node.left = self.helper(nums, start, mid - 1)
        node.right = self.helper(nums, mid + 1, end)
        return node


