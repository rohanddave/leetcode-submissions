# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(head): 
            length = 0
            while head: 
                length += 1
                head = head.next
            return length

        def move_by_k(head, k): 
            for _ in range(k): 
                head = head.next
            return head
        
        len_a, len_b = get_length(headA), get_length(headB)
        if len_a > len_b:
            headA = move_by_k(headA, len_a - len_b)
        elif len_b > len_a: 
            headB = move_by_k(headB, len_b - len_a)
        
        while headA and headB: 
            if headA is headB:
                return headA 
            headA = headA.next
            headB = headB.next

        return None

