# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def build(head): 
            if not head:
                return None 
            
            prev = None
            slow = fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            mid = slow 
            # disconnect two lists
            if prev:
                prev.next = None
            tmp = mid.next
            mid.next = None
            root = TreeNode(mid.val)
            if mid != head:
                root.left = build(head)
            root.right = build(tmp)
            return root
        
        return build(head)


        