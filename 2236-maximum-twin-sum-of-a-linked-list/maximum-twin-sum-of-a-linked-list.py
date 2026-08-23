# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def get_len(head): 
            n = 0 
            while head:
                n += 1
                head = head.next
            return n 
        
        def reverse(head): 
            prev = None 
            curr = head 
            while curr: 
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        
        n = get_len(head) 
        curr = head
        for _ in range((n // 2) - 1):
            curr = curr.next
        
        n2 = curr.next
        curr.next = None
        n1, n2 = head, reverse(n2)

        res = float('-inf')
        while n1 and n2: 
            res = max(res, n1.val + n2.val)
            n1 = n1.next 
            n2 = n2.next
        return res


        


        