"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        answer = 0
        def dfs(node):
            nonlocal answer
            best = 0 
            second = 0 

            for child in node.children: 
                height = dfs(child)
                if height > best: 
                    second = best 
                    best = height 
                elif height > second: 
                    second = height 
            
            answer = max(answer, 1 + best + second)
            return 1 + best 
        dfs(root)
        return answer - 1
