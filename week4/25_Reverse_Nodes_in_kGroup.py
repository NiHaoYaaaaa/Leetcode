# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        answer = head
        last_one = None
        nowNode = head
        nums = 0
        while(nowNode):
            nums += 1
            if nums == k:    
                tail = last_one.next if last_one else head
                pre = tail
                tmp = pre.next
                nxt = tmp.next
                for i in range(k-2):
                    tmp.next = pre
                    pre = tmp
                    tmp = nxt
                    nxt = nxt.next
                tail.next = nxt
                nowNode.next = pre
                if last_one: 
                    last_one.next = nowNode
                else:
                    answer = nowNode
                last_one = tail
                nowNode = tail.next
                nums = 0
            else:
                nowNode = nowNode.next
        return answer