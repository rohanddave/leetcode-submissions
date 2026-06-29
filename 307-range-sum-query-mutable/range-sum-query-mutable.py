class TreeNode: 
    def __init__(self, l, r, val=0, left=None, right=None):
        self.l = l 
        self.r = r
        self.val = val
        self.left = left 
        self.right = right 
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self._build(nums, 0, len(nums) - 1)
    
    def _build(self, nums, l, r): 
        node = TreeNode(l, r)
        if l == r:
            node.val = nums[l]
            return node
        
        m = (l + r) // 2
        node.left = self._build(nums, l, m)
        node.right = self._build(nums, m + 1, r)

        node.val = node.left.val + node.right.val
        return node

    def update(self, index: int, val: int) -> None:
        def update(node, idx, val): 
            if node.l == node.r:
                node.val = val
                return 
            
            mid = (node.l + node.r) // 2
            if idx <= mid:
                update(node.left, idx, val)
            else:
                update(node.right, idx, val)
            
            node.val = node.left.val + node.right.val 
            return
        update(self.root, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        def query(node, ql, qr):
            if qr < node.l or ql > node.r:
                return 0
            if ql <= node.l and qr >= node.r:
                return node.val
            
            return query(node.left, ql, qr) + query(node.right, ql, qr)
        return query(self.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)