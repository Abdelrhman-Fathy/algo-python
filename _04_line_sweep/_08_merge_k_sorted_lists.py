# Definition for singly-linked list.
import heapq
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def mergeKLists(lists):
        result = ListNode()
        head = result
        heap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while len(heap) > 0:
            result.next = ListNode()
            result = result.next
            result.val = heap[0][0]
            i = heap[0][1]
            heapq.heappop(heap)
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next

def test():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]