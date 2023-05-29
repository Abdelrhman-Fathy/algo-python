#https://leetcode.com/problems/binary-tree-level-order-traversal/
from queue import Queue
def levelOrder(root):
    return bfs(root)
def bfs(root):
    result = []
    if root is None:
        return result
    q = Queue()
    q.put(root)
    while not q.empty():
        nodes_count = q.qsize()
        temp = []
        for _ in range(nodes_count):
            node = q.get()
            temp.append(node.val)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        result.append(temp)
    return result


