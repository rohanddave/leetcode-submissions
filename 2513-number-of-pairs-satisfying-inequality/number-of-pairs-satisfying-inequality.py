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
    
    def _build(self, l ,r): 
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
        
        return self.query(node.left, ql, qr) + self.query(node.right, ql, qr)
    
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

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        '''
        goal: return number of pairs (i, j) where nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff 

        observations: 
        - 0 indexed arrays num1 and nums2
        - pair(i,j) nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff 
        - for a fixed index j 
        nums1[i] - num2[i] <= nums1[j] - nums2[j] + diff
        nums1[i] - num2[i] - diff <= nums1[j] - nums2[j]

        approach: 
        - move j pointer from left to right 
        - count number of indices i where nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff
        - use a segment tree to query this 
        - use a segment tree to update nums1[j]- nums2[j]
        '''
        n = len(nums1)
        sorted_diff = sorted(set([nums1[i] - nums2[i] for i in range(n)]))
        rank = {val: idx + 1 for idx, val in enumerate(sorted_diff)}
        seg_tree = SegmentTree(len(rank)) # TODO: this will store the frequency of difference between nums1 and nums2 at each index i.e. nums1[k] - nums2[k]. this will need co-ordinate compression 

        count = 0
        for j in range(n):
            target = nums1[j] - nums2[j] + diff
            ql, qr = 1, bisect_right(sorted_diff, target)
            count += seg_tree.query(seg_tree.root, ql, qr)
            seg_tree.update(seg_tree.root, rank[nums1[j] - nums2[j]], 1)
        return count



        