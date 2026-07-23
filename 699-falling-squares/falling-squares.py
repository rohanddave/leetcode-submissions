class TreeNode: 
    def __init__(self, l, r, val=0, left=None, right=None):
        self.l = l
        self.r = r
        self.val = val
        self.left = left
        self.right = right 

class SegmentTree:
    def __init__(self, n): 
        self.root = self._build(1, n)
    
    def _build(self, l, r): 
        node = TreeNode(l, r)
        if l == r:
            return node 
        m = (l + r) // 2
        node.left = self._build(l, m)
        node.right = self._build(m + 1, r)
        node.val = max(node.left.val, node.right.val)
        return node
    
    def query(self, node, ql, qr): 
        if ql <= node.l and qr >= node.r: 
            return node.val 
        if ql > node.r or qr < node.l:
            return 0 
        
        return max(self.query(node.left, ql, qr), self.query(node.right, ql, qr))
    
    def update(self, node, ql, qr, val): 
        if ql > node.r or qr < node.l:
            return
        
        if node.l == node.r:
            node.val = val 
            return 
        
        self.update(node.left, ql, qr, val)
        self.update(node.right, ql, qr, val)
        node.val = max(node.left.val, node.right.val)
        return 

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        '''
        goal: return ans arr where ans[i] is the tallest stack of squares 

        observations: 
        - when a square falls only [left, left + side] positions height changes 
        - points on x axis could be any positive number 
        - a square lands on the highest point between [left, left + side] and all the point's height becomes highest point + height of new square

        approach: 
        - use a segment tree to update the heights of points from [left, left + side)
        - track the highest point for every square. max(prev, new_height)
        - segment tree stores the max height 
        - indices are all boundry points for all squares     
        '''

        boundary = [] 
        for left, side in positions: 
            boundary.extend([left, left + side])
        
        coords = sorted(set(boundary))
        rank = {x: i + 1 for i, x in enumerate(coords)}

        seg_tree = SegmentTree(len(rank))
        ans = [0] * len(positions)

        for i, (left, side) in enumerate(positions): 
            start, end = left, left + side
            ql, qr = rank[start], rank[end] - 1
            curr_height = seg_tree.query(seg_tree.root, ql, qr) 
            new_height = curr_height + side
            ans[i] = max(ans[i - 1] if i != 0 else 0, new_height)
            seg_tree.update(seg_tree.root, rank[start], rank[end] - 1, new_height)
        return ans
        
        