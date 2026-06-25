# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node): 
            if not node:
                return 0, None 
            
            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)

            # this is the LCA of deepest leaves rooted at node
            if left_height == right_height:
                return 1 + left_height, node
            elif left_height < right_height: 
                return 1 + right_height, right_lca 
            else: 
                return 1 + left_height, left_lca
        return dfs(root)[1]
