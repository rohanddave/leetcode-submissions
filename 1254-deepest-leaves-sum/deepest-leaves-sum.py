# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        max_depth = 0
        def dfs(node, depth):
            nonlocal res, max_depth 
            if not node:
                return
            if not node.left and not node.right: 
                if depth == max_depth:
                    res += node.val
                elif depth > max_depth:
                    res = node.val
                    max_depth = depth
                return
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res
        