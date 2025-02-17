# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        o = head
        e = eh = head.next
        
        while e and o and e.next and o.next:
            o.next = e.next
            o = o.next      
            e.next = o.next
            e = e.next  
        o.next = eh


        return head