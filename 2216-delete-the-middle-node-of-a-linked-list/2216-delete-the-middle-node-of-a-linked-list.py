# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return None

        p = None #previous
        s = f = head # slow pointer, fast pointer
        while f and f.next:
            p = s
            s = s.next
            f = f.next.next
        
        p.next = s.next
        return head