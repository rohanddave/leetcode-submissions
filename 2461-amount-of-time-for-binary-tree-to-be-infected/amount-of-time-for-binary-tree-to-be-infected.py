# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_map = {} 
        start_node = None
        def dfs(node, parent): 
            nonlocal start_node
            if not node:
                return 
            
            if node.val == start:
                start_node = node
            if parent:
                parent_map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)

        q = collections.deque([(0, start_node)]) # time, node 
        infected = {start_node} 
        res = float('-inf')

        while q: 
            time, node = q.popleft() 
            res = max(res, time)

            if node in parent_map and parent_map[node] not in infected: 
                q.append((time + 1, parent_map[node]))
                infected.add(parent_map[node])
            if node.left and node.left not in infected: 
                q.append((time + 1, node.left))
                infected.add(node.left)
            if node.right and node.right not in infected: 
                q.append((time + 1, node.right))
                infected.add(node.right)
        
        return res