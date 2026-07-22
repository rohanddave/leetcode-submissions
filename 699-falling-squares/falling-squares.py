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
    
    def update(self, node, ql, qr, new_val): 
        if ql > node.r or qr < node.l:
            return 
        
        if node.l == node.r:
            node.val = new_val 
            return 

        self.update(node.left, ql, qr, new_val)
        self.update(node.right, ql, qr, new_val)
        node.val = max(node.left.val, node.right.val)
        return

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        '''
        problem: 
        - positions[i] = [x coordinate of left edge, side length]
        
        goal: return ans where ans[i] is the tallest height after dropping ith square

        observations:
        - square height influence is in the range [left, left + side)
        
        approach: 
        - for the height of the stack we need the max existing y height in the range [left, left + side)
        '''
        boundaries = []
        for left, side in positions: 
            boundaries.extend([left, left + side])
        
        coords = sorted(set(boundaries))
        rank = {x: i + 1 for i, x in enumerate(coords)}

        seg_tree = SegmentTree(len(rank))
        ans = [0] * len(positions)

        for i, (left, side) in enumerate(positions):
            start, end = left, left + side
            ql, qr = rank[left], rank[end] - 1
            base = seg_tree.query(seg_tree.root, ql, qr)
            
            new_height = base + side
            seg_tree.update(seg_tree.root, ql, qr, new_height)
            # for point in range(start, end): 
            #     if point in rank: 
            #         seg_tree.update(seg_tree.root, rank[point], rank, new_height)
            
            ans[i] = max(new_height, 0 if i == 0 else ans[i - 1])
            
        return ans


        