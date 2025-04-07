# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        begin = head
        while(begin.next):
            begin.val, begin.next.val = begin.next.val, begin.val
            if begin.next.next: begin = begin.next.next
            else: break
        return head