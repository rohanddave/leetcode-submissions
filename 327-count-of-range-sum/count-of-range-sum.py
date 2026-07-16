class TreeNode:
    def __init__(self, l, r, val=0, left=None, right=None):
        self.l = l 
        self.r = r
        self.val = val 
        self.left = left 
        self.right = right 
    
class SegmentTree:
    def __init__(self, n): 
        self.root = self._build(0, n - 1)
    
    def _build(self, l, r): 
        node = TreeNode(l, r)
        if l == r:
            return node 
        
        m = (l + r) // 2
        node.left = self._build(l, m)
        node.right = self._build(m + 1, r)
        node.val = node.left.val + node.right.val
        return node
    
    def query(self, node, ql, qr): 
        if ql <= node.l and qr >= node.r:
            return node.val 
        if ql > node.r or qr < node.l:
            return 0
    
        left = self.query(node.left, ql, qr)
        right = self.query(node.right, ql, qr)
        return left + right
    
    def update(self, node, idx, delta): 
        if node.l == node.r: 
            node.val += delta 
            return 
        
        m = (node.l + node.r) // 2
        if idx <= m:
            self.update(node.left, idx, delta) 
        else:
            self.update(node.right, idx, delta)
        
        node.val = node.left.val + node.right.val
        return
    
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])
        
        sorted_prefix = sorted(set(prefix))
        rank = { 
            val: idx
            for idx, val in enumerate(sorted_prefix)
        }
        seg_tree = SegmentTree(len(rank) + 1)

        count = 0
        for p in prefix: 
            left_boundry = p - upper 
            right_boundry = p - lower

            ql, qr = bisect_left(sorted_prefix, left_boundry), bisect_right(sorted_prefix, right_boundry) - 1
            count += seg_tree.query(seg_tree.root, ql, qr)
            seg_tree.update(seg_tree.root, rank[p], 1)
        
        return count
        