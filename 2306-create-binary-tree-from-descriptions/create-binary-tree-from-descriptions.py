# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapping = {} 
        parent_map = {}

        for parent_val, child_val, is_left in descriptions:
            parent = TreeNode(parent_val) if parent_val not in mapping else mapping[parent_val]
            child = TreeNode(child_val) if child_val not in mapping else mapping[child_val]
            if is_left:
                parent.left = child
            else: 
                parent.right = child 
            mapping[parent_val] = parent
            mapping[child_val] = child 
            parent_map[child] = parent
        
        root = None 
        parent_val, child_val, _ = descriptions[0]
        curr, child = mapping[parent_val], mapping[child_val]
        while curr:
            child = curr
            curr = parent_map[curr] if curr in parent_map else None
        return child
            


        