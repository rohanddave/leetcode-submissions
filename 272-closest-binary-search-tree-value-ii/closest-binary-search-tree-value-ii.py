# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode | None, target: float, k: int) -> list[int]:
        heap = [] 

        def dfs(node): 
            if not node:
                return 
            
            heapq.heappush(heap, (-1 * abs(target - node.val), node.val))
            if len(heap) > k:
                heapq.heappop(heap)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return [val for _, val in heap]
        
        