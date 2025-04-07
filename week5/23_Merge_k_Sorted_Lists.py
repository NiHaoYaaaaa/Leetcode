# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        
        head = ListNode(-1)
        current = head

        while(heap):
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = node
            if node.next:
                next_val = node.next.val
                heapq.heappush(heap, (next_val, idx, node.next))
        
        return head.next

        