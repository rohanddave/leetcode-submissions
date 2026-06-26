# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        '''
        observations:
        - the shortest path from a node to another is throught it's LCA 
        - path from start will always be upwards till the LCA 
        - path from LCA to destination will be downwards / path from destination to LCA will be upwards. we cannot travel from the LCA to the destination in a downard path without trying all combinations. Instead if we travel from the destination to LCA upwards we just need to handle the path instruction to be reversed

        we're given just the root of the tree means we cannot travel up from the two nodes. 
        we need to find the LCA of the two nodes first


        start -> LCA
        reverse(end -> LCA)

        
        '''
        def dfs(node): 
            if not node or node.val == startValue or node.val == destValue: 
                return node
            
            left = dfs(node.left) 
            right = dfs(node.right) 

            if left and right:
                return node 
            if left: 
                return left
            if right:
                return right 
            return None
        lca = dfs(root)
        
        def find_path(node, target, path): 
            if not node:
                return False 
            if node.val == target:
                return True 
            
            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()
        
            return False
        
        start_path = []
        find_path(lca, startValue, start_path)
        end_path = []
        find_path(lca, destValue, end_path)
        return "U" * len(start_path) + ''.join(end_path)

