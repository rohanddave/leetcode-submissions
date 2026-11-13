# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode(-1, head) 
        prev, curr, nex = dummy, head, head.next

        while nex: 
            delete_curr = False
            while nex and curr.val == nex.val:
                delete_curr = True
                nex = nex.next
                
            curr.next = nex

            if delete_curr: 
                prev.next = nex
            else: 
                prev = curr
            curr = nex
            nex = curr.next if curr is not None else None
        
        return dummy.next
        