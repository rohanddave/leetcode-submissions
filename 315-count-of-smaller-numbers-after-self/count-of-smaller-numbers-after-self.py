
class FenwickTree: 
    def __init__(self, n): 
        self.tree = [0] * (n + 1)
    
    def query(self, i): 
        ans = 0 
        while i > 0:
            ans += self.tree[i]
            i -= i & -i 
        return ans
    
    def update(self, i, delta):
         while i < len(self.tree):
            self.tree[i] += delta 
            i += i & -i

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # coordinate compression for fenwick tree 
        rank = {}
        sorted_list = sorted(set(nums))
        for i, num in enumerate(sorted_list): 
            rank[num] = i + 1
        
        fenwick_tree = FenwickTree(len(sorted_list))

        answer = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            r = rank[nums[i]]
            answer[i] = fenwick_tree.query(r - 1)
            fenwick_tree.update(rank[nums[i]], 1)
        
        return answer
        