# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def get_height(node): 
            if not node:
                return 0 
            
            left = get_height(node.left)
            right = get_height(node.right)
            return 1 + max(left, right)
        
        height = get_height(root)
        res = 0 
        def collect_deepest_leaves(node, h):
            nonlocal res 
            if not node:
                return 
            if not node.left and not node.right:
                if h == height:
                    res += node.val 
                return 
            
            collect_deepest_leaves(node.left, h + 1)
            collect_deepest_leaves(node.right, h + 1)
        
        collect_deepest_leaves(root, 1)
        return res
        