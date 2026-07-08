# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def is_leaf(node):
            return node and (not node.left and not node.right)
        
        left = []
        def left_boundry(node):
            if not node or is_leaf(node): 
                return 
            left.append(node.val)
            if node.left:
                left_boundry(node.left)
            elif node.right:
                left_boundry(node.right)

        right = [] 
        def right_boundry(node):
            if not node or is_leaf(node):
                return
            
            right.append(node.val)
            if node.right:
                right_boundry(node.right)
            elif node.left:
                right_boundry(node.left)
        
        leaves = [] 
        def collect_leaves(node):
            if not node:
                return 
            
            if is_leaf(node):
                leaves.append(node.val)
            
            collect_leaves(node.left)
            collect_leaves(node.right)
        
        if is_leaf(root):
            return [root.val]
            
        left_boundry(root.left)
        right_boundry(root.right)
        collect_leaves(root)

        return [root.val] + left + leaves + right[::-1]


        