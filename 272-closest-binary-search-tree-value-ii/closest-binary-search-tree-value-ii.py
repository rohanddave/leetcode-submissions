# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode | None, target: float, k: int) -> list[int]:
        # APPROACH 1:
        # heap = [] 

        # def dfs(node): 
        #     if not node:
        #         return 
            
        #     heapq.heappush(heap, (-1 * abs(target - node.val), node.val))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return [val for _, val in heap]

        # APPROACH 2:
        inorder = [] 

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left) 
            inorder.append(node.val)
            dfs(node.right)
        
        dfs(root)

        l, r = 0, len(inorder)
        while l < r:
            m = (l + r) // 2
            if inorder[m] >= target:
                r = m
            else:
                l = m + 1
        
        i, j = l - 1, l
        res = []
        for _ in range(k):
            diff_i = abs(target - inorder[i]) if i >= 0 else float('inf')
            diff_j = abs(target - inorder[j]) if j < len(inorder) else float('inf')
            if diff_i < diff_j:
                res.append(inorder[i])
                i -= 1
            else: 
                res.append(inorder[j])
                j += 1
        return res
        
            
            

        
        