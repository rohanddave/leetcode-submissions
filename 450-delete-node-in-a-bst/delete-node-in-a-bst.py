# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            curr = node 
            while curr.left: 
                curr = curr.left
            return curr 
        
        def delete(node, key): 
            if not node:
                return None
            
            if key < node.val: 
                node.left = delete(node.left, key)
            elif key > node.val:
                node.right = delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                successor = find_min(node.right)
                node.val = successor.val 
                node.right = delete(node.right, node.val)
            
            return node
        return delete(root, key)
        
        