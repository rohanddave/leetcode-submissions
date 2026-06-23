# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode() 
        curr = dummy 

        heap = []
        for i, head in enumerate(lists): 
            if head: 
                heapq.heappush(heap, (head.val, i, head))
    
        while heap: 
            _, list_idx, node = heapq.heappop(heap) 
            curr.next = node 
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        return dummy.next 

        


        