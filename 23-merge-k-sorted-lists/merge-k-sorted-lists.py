# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []

        for idx, head in enumerate(lists): 
            if head:
                heapq.heappush(heap, (head.val, idx, head))

        dummy = ListNode()
        curr = dummy

        while heap: 
            _, idx, node = heapq.heappop(heap)
            curr.next = node 
            curr = node

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next


        