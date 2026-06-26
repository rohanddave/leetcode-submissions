"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set() 
        def climb(node): 
            if not node:
                return 
            seen.add(node)
            climb(node.parent)
        
        climb(p)
        res = None
        def lca(node): 
            nonlocal res 
            if not node:
                return 
            if node in seen and res is None:
                res = node
                return 
            
            lca(node.parent)
        lca(q)
        return res
            