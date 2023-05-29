#https://leetcode.com/problems/path-sum/
#112. Path Sum
global_box = False
def hasPathSum(self, root, targetSum):
    self.dfs(root, targetSum)
    return self.global_box
def dfs(self, node, target, global_box):
    if node is None:
        return
        # backtracking case
    if self.global_box:
        return
        # base case : leaf node
    if node.left is None and node.right is None:
        if target == node.val:
            self.global_box = True
        return
        # recursive case : internal node
    if node.left is not None:
        self.dfs(node.left, target - node.val)
    if node.right is not None:
        self.dfs(node.right, target - node.val)




# Recursive case