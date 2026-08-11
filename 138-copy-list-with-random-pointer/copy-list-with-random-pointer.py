"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {} 

        def copy(node): 
            if not node:
                return None 
            if node in mapping: 
                return mapping[node]
            
            new_node = Node(node.val)
            mapping[node] = new_node
            new_node.next = copy(node.next)
            new_node.random = copy(node.random)
            return new_node
        
        return copy(head)
        