#https://leetcode.com/problems/count-univalue-subtrees/
#leetcode 250 Count Univalue Subtrees - LeetCode


class Solution:
    global_count = 0
    def countUnivalSubtrees(self, root):
        self.global_count = 0
        self.dfs(root)
        return self.global_count
    def dfs(self, node):
        #edge case
        if node is None:
            return True
        #base case:leaf node
        if node.left is None and node.right is None:
            self.global_count+=1
            return True
        #recursive case: internal node
        unival = True
        if node.left is not None:
            left = self.dfs(node.left)
            if left is False or node.val != node.left.val:
                unival = False
        if node.right is not None:
            right = self.df(node.right)
            if right is False or node.val != node.right.val:
                unival = False
        if unival:
            self.global_count += 1
        return unival
