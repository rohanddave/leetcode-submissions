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
        node.val = node.left.val + node.right.val 
        return node
    
    def query(self, node, ql, qr): 
        if ql <= node.l and qr >= node.r: 
            return node.val
        if node.l > qr or node.r < ql:
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
        return

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        '''
        problem: 
        - create sorted array from elements in instructions 
        - start with empty nums array
        - cost of insertion = min(count of elements in nums < instructions[i], count of elements in nums > instructions[i])
        - find total cost % 10**9 + 7

        goal: return total cost to create sorted array

        observations: 
        - cost1 = # elements < instructions[i]; cost2 = # elements > instructions[i]
        - a simple binary search would work but that would mean populating then nums array in sorted order which would be O(n) making total time O(n^2) 
        
        approach: 
        - use a segment tree that stores frequencies of elements in instructions
        - use co-ordinate compression bc seg tree needs ranges values could be [1, inf]
        - keep updating values in seg tree as you move left to right in instructions => update(root, rank[instructions[i]], 1)
        - cost = query(root, 0, rank[last_lt(instructions[i])]) + query(root, first_gt(instructions[i]), inf)
        '''
        MOD = 10**9 + 7
        sorted_instructions = sorted(set(instructions)) 
        rank = {val: idx + 1 for idx, val in enumerate(sorted_instructions)}

        seg_tree = SegmentTree(len(rank))
        cost = 0
        for instruction in instructions:
            lt_ql, lt_qr = 0, rank[instruction] - 1
            gt_ql, gt_qr = rank[instruction] + 1, float('inf')

            lt_cost = seg_tree.query(seg_tree.root, lt_ql, lt_qr)
            gt_cost = seg_tree.query(seg_tree.root, gt_ql, gt_qr)
            cost +=  min(lt_cost, gt_cost)

            seg_tree.update(seg_tree.root, rank[instruction], 1)
        return cost % MOD