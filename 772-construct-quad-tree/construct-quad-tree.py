"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        '''
        goal: construct quad tree from grid and return the root 

        rules of construction: 
        - if subgrid has all same values: isLeaf = True and val = 0 or 1 (value of the element)
        - if subgrid has diff values: isLeaf = False and val = any value
        
        observations: 
        - each 1x1 cell is a leaf 
        - if all 4 children are leaves with same values then merge into one big leaf 
        '''
        m, n = len(grid), len(grid[0])

        def build(row1, col1, row2, col2):
            # if size < 1
            if row2 < row1 or col2 < col1:
                return None
            # if size == 1
            if row1 == row2 and col1 == col2:
                return Node(grid[row1][col1], True, None, None, None, None)
            
            row_mid = (row1 + row2) // 2
            col_mid = (col1 + col2) // 2

            children = [
                build(row1, col1, row_mid, col_mid), # top left 
                build(row1, col_mid + 1, row_mid, col2), # top right 
                build(row_mid + 1, col1, row2, col_mid), # bottom left 
                build(row_mid + 1, col_mid + 1, row2, col2) # bottom right
            ]

            if all(child.isLeaf for child in children) and all(child.val == children[0].val for child in children):
                return Node(children[0].val, True, None, None, None, None)
            
            return Node(0, False, children[0], children[1], children[2], children[3])
        return build(0, 0, m - 1, n - 1)

            
            
        