# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left = [] 
        def collect_left(node): 
            if not node or (not node.left and not node.right):
                return
            left.append(node.val) 
            if node.left: 
                collect_left(node.left)
            elif node.right: 
                collect_left(node.right)
        
        right = []
        def collect_right(node):
            if not node or (not node.left and not node.right):
                return 
            
            right.append(node.val)
            if node.right: 
                collect_right(node.right)
            elif node.left:
                collect_right(node.left)

        leaves = []
        def collect_leaves(node): 
            if not node:
                return 
            
            if not node.left and not node.right:
                leaves.append(node.val)
            
            collect_leaves(node.left)
            collect_leaves(node.right)
        
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        collect_left(root.left)
        collect_right(root.right)
        collect_leaves(root)

        return [root.val] + left + leaves + right[::-1] 

            

            
        