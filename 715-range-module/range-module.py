'''
problem: 
- design DS to track half open interval ranges 
- addRange(left, right): adds half open [left,right). 
- queryRange(left, right): returns true if every number in [left, right) is tracked 
- removeRange(left, right): stops tracking every number currently number in [left, right)

observations: 
- half open interval means we add [left, right - 1]
- addRange:
    - if entire interval exists: do nothing 
    - if partial interval exsists: merge into one larger 
    - if no overlapping interval exists: insert into correct position
- queryRange: 
    - if entire interval exists: return true 
    - if no overlap: return false 
    - if partial interval exists: return left and right 
- removeRange: 
    - 
'''
class TreeNode: 
    def __init__(self, l, r, covered=False, left=None, right=None):
        self.l = l 
        self.r = r 
        self.covered = covered 
        self.left = left 
        self.right = right 

class SegmentTree:
    def __init__(self): 
        self.root = TreeNode(1, 10**9)
    
    def split(self, node):  
        # some base case 
        if node.left is not None: 
            return
        
        m = (node.l + node.r) // 2
        node.left = TreeNode(node.l, m, node.covered)
        node.right = TreeNode(m, node.r, node.covered)
    
    def update(self, node, ql, qr, val): 
        # if no overlap
        if ql >= node.r or qr <= node.l:
            return 
        # if full overlap
        if ql <= node.l and qr >= node.r: 
            node.covered = val
            node.left = None 
            node.right = None
            return 

        # if partial overlap
        self.split(node)
        self.update(node.left, ql, qr, val)
        self.update(node.right, ql, qr, val)
        node.covered = node.left.covered and node.right.covered
    
    def query(self, node, left, right): 
        if left <= node.l and right >= node.r:
            return node.covered 
        
        if node.left is None:
            return node.covered 
        
        m = (node.l + node.r) // 2
        if right <= m:
            return self.query(node.left, left, right)
        if left >= m:
            return self.query(node.right, left, right)

        return self.query(node.left, left, m) and self.query(node.right, m, right)

class RangeModule:
    def __init__(self):
        self.seg_tree = SegmentTree()    

    def addRange(self, left: int, right: int) -> None:
        self.seg_tree.update(self.seg_tree.root, left, right, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.seg_tree.query(self.seg_tree.root, left, right)        

    def removeRange(self, left: int, right: int) -> None:
        self.seg_tree.update(self.seg_tree.root, left, right, False)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)