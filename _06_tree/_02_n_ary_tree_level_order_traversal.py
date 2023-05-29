#https://leetcode.com/problems/n-ary-tree-level-order-traversal
#429. N-ary Tree Level Order Traversal
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
            for child in node.children:
                q.put(child)
        result.append(temp)
    return result


