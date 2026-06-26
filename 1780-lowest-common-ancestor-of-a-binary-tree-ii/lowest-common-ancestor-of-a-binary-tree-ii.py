# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None 
        def dfs(node):
            nonlocal lca
            if not node:
                return 0 
            
            left_count = dfs(node.left)
            right_count = dfs(node.right)

            count = left_count + right_count + (1 if node is p or node is q else 0)
            if count == 2 and lca is None: 
                lca = node 
            return count
        dfs(root)
        return lca