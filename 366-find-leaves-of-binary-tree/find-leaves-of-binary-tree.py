# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, leaves):
            if not node:
                return None
            if not node.left and not node.right: 
                leaves.append(node.val)
                return None
            
            node.left = dfs(node.left, leaves)
            node.right = dfs(node.right, leaves)
            return node
        
        curr = root 
        while curr: 
            res.append([])
            curr = dfs(curr, res[-1])
        
        return res
        

        