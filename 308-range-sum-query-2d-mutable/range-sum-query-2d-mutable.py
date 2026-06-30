class TreeNode:
    def __init__(self, l, r, val=0):
        self.l = l 
        self.r = r 
        self.val = val
        self.children = []

class SegmentTree:
    def __init__(self, mat):
        m, n = len(mat), len(mat[0])
        self.root = self._build((0, 0), (m - 1, n - 1), mat)
    
    def _build(self, l, r, mat):
        node = TreeNode(l, r)
        row1, col1 = l 
        row2, col2 = r
        if l == r: 
            node.val = mat[l[0]][l[1]]
            return node
        
        row_mid = (row2 + row1) // 2
        col_mid = (col2 + col1) // 2

        children = [
            ((row1, col1), (row_mid, col_mid)), # top left
            ((row1, col_mid + 1), (row_mid, col2)), # top right
            ((row_mid + 1, col1), (row2, col_mid)), # bottom left 
            ((row_mid + 1, col_mid + 1), (row2, col2)), # bottom right
        ]

        for child_l, child_r in children: 
            if child_l[0] <= child_r[0] and child_l[1] <= child_r[1]:
                node.children.append(self._build(child_l, child_r, mat))

        for child in node.children: 
            node.val += child.val

        return node
    
    def query(self, l, r): 
        def helper(node, l, r): 
            def no_overlap(tl1, br1, tl2, br2):
                def to_left(tl1, br1, tl2, br2): 
                    return br2[1] < tl1[1]
                def to_right(tl1, br1, tl2, br2):
                    return tl2[1] > br1[1]
                def is_above(tl1, br1, tl2, br2): 
                    return br2[0] < tl1[0]
                def is_below(tl1, br1, tl2, br2): 
                    return tl2[0] > br1[0]
                
                return to_left(tl1, br1, tl2, br2) or to_right(tl1, br1, tl2, br2) or is_above(tl1, br1, tl2, br2) or is_below(tl1, br1, tl2, br2)
        
            def full_overlap(node_l, node_r, q_l, q_r): 
                top_left_within_bounds = q_l[0] <= node_l[0] <= q_r[0] and q_l[1] <= node_l[1] <= q_r[1]
                bottom_right_within_bounds =  q_l[0] <= node_r[0] <= q_r[0] and q_l[1] <= node_r[1] <= q_r[1]
                return top_left_within_bounds and bottom_right_within_bounds
            
            if no_overlap(node.l, node.r, l, r):
                return 0
            if full_overlap(node.l, node.r, l, r):
                return node.val 
            
            ans = 0 
            for child in node.children: 
                ans += helper(child, l, r)
            return ans
        return helper(self.root, l, r)

    def update(self, row, col, val):
        def contains(node): 
            return node.l[0] <= row <= node.r[0] and node.l[1] <= col <= node.r[1]
        
        def helper(node): 
            if node.l == node.r: 
                node.val = val
                return 
            
            for child in node.children: 
                if contains(child): 
                    helper(child)
                
            node.val = sum(child.val for child in node.children)
        
        helper(self.root)
                

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.seg_tree = SegmentTree(matrix)        

    def update(self, row: int, col: int, val: int) -> None:
        self.seg_tree.update(row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.seg_tree.query((row1, col1), (row2, col2))
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)