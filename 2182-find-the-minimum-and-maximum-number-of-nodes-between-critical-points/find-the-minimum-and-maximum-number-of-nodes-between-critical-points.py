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
        critical_points = []
        while nex:
            if not prev: 
                critical_points.append(-1)
            else: 
                if curr.val < prev.val and curr.val < nex.val: # minima
                    critical_points.append(idx)
                elif curr.val > prev.val and curr.val > nex.val: # maxima
                    critical_points.append(idx)
                               
            idx += 1
            tmp = nex.next
            prev = curr 
            curr = nex
            nex = tmp
        print(critical_points)

        res = [float('inf'), float('-inf')]

        for i in range(len(critical_points) - 1):
            res[0] = min(res[0], critical_points[i + 1] - critical_points[i])
        
        if len(critical_points) > 1: 
            res[1] = critical_points[-1] - critical_points[0]
        
        if res[0] == float('inf'):
            res[0] = -1
        if res[1] == float('-inf'):
            res[1] = -1

        return res
            
