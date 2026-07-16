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
            node.val = 0
            return node
        
        m = (l + r) // 2
        node.left = self._build(l, m)
        node.right = self._build(m + 1, r)
        node.val = node.left.val + node.right.val 
        return node
    
    def query(self, node, ql, qr):
        if ql <= node.l and qr >= node.r: 
            return node.val 
        if node.l > qr or node.r < ql:
            return 0 
        
        left = self.query(node.left, ql, qr)
        right = self.query(node.right, ql, qr)
        return left + right        
    
    def update(self, node, i, delta): 
        if node.l == node.r:
            node.val += delta 
            return 
        
        mid = (node.l + node.r) // 2
        if i <= mid: 
            self.update(node.left, i, delta)
        else: 
            self.update(node.right, i, delta)
        
        node.val = node.left.val + node.right.val
    
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        rank = {
            val: i + 1 for i, val in enumerate(sorted_nums)
        }

        seg_tree = SegmentTree(len(rank))
        count = 0 
        for j in range(len(nums)):
            idx = rank[nums[j]]
            ql, qr = bisect_right(sorted_nums, 2 * nums[j]), float('inf')
            count += seg_tree.query(seg_tree.root, ql + 1, qr)
            seg_tree.update(seg_tree.root, idx, 1)
        
        return count
        