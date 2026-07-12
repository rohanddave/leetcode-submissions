class TreeNode: 
    def __init__(self, l, r, maximum=None, left=None, right=None):
        self.l = l
        self.r = r
        self.maximum = maximum 
        self.left = left 
        self.right = right

class SegmentTree:
    def __init__(self, arr):
        self.root = self._build(0, len(arr) - 1, arr)

    def _build(self, l, r, arr): 
        node = TreeNode(l, r)
        if l == r:
            node.maximum = arr[l]
            return node

        m = (l + r) // 2
        node.left = self._build(l, m, arr) 
        node.right = self._build(m + 1, r, arr)

        node.maximum = max(node.left.maximum, node.right.maximum)
        return node
    
    def query(self, val): 
        def helper(node): 
            if node.l == node.r:
                return node.l if node.maximum >= val else -1
            
            if node.left.maximum >= val: 
                return helper(node.left)
            elif node.right.maximum >= val:
                return helper(node.right)
            return -1
        return helper(self.root)
    
    def update(self, idx, val):
        def helper(node):
            if node.l == node.r:
                node.maximum = 0
                return 
            
            m = (node.l + node.r) // 2
            if idx <= m:
                helper(node.left)
            else:
                helper(node.right)

            node.maximum = max(node.left.maximum, node.right.maximum)
        helper(self.root)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg_tree = SegmentTree(baskets)
        count = 0

        for fruit in fruits: 
            idx = seg_tree.query(fruit)
            if idx == -1:
                count += 1
            else: 
                seg_tree.update(idx, 0)
        return count

        