# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fh = sh = head
        prev = None
        while fh and fh.next:
            fh = fh.next.next  # moving twice as fast as sh to find the middle node
            tmp = sh.next # moving one node at a time, assigning to temporary node to swap
            sh.next = prev #  assiging previous node to slow head's next
            prev = sh # assigning slow head to previous node
            sh = tmp # assiging temp(earlier slow head's next to temp) to slow head -- moving one node at a time
        
        res = 0
        while sh:
            res = max(res, sh.val+prev.val)
            sh = sh.next
            prev = prev.next
        
        return res