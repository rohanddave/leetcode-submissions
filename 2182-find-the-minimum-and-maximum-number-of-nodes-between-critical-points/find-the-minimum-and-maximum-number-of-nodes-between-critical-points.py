# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        prev, curr, nex = head, head.next, head.next.next
        idx = 1
        earliest_critical_point_idx, prev_critical_point_idx = None, None
        res = [float('inf'), -1]
        while nex:
            if (curr.val < prev.val and curr.val < nex.val) or (curr.val > prev.val and curr.val > nex.val):
                curr_critical_point_idx = idx
                # possible to calculate the max distance
                if earliest_critical_point_idx is not None: 
                    res[1] = curr_critical_point_idx - earliest_critical_point_idx
                
                # possible to calcualte min distance
                if prev_critical_point_idx is not None: 
                    res[0] = min(res[0], curr_critical_point_idx - prev_critical_point_idx)

                if earliest_critical_point_idx is None:
                    earliest_critical_point_idx = curr_critical_point_idx
                prev_critical_point_idx = curr_critical_point_idx

            idx += 1
            tmp = nex.next
            prev = curr 
            curr = nex
            nex = tmp
        
        if res[0] == float('inf'):
            res[0] = -1
        return res
            
