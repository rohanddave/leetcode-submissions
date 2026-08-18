# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        observations: 
        - the value added to a node will be the sum of the right subtree 
        - if the node is a left child of a node then the parent sum would be passed down it's entire subtree too 
        '''
        running_sum = 0 
        def dfs(node): 
            nonlocal running_sum
            if not node:
                return 
            
            dfs(node.right) 
            tmp = node.val 
            
            node.val += running_sum
            running_sum += tmp 
            dfs(node.left)
            return
        
        dfs(root)
        return root
        