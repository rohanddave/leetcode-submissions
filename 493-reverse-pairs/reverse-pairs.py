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
    def reversePairs(self, nums: List[int]) -> int:
        '''
        problem: 
        - reverse pair (i, j)
            - 0 <= i < j 
            - nums[i] > 2 * nums[j]
        
        goal: return number of reverse pairs in array

        observations:
        - for nums[j] we need to pair with i's (before j) that are greater than 2 * nums[j]
        - so we need to know all the numbers before nums[j] that are greater than 2 * nums[j]
        - bottleneck is rescanning from 0 - j to find ith element 

        approach: 
        - scan left to right 
        - fenwick tree answers prefix sum i.e. how many values <= target
        - query for (2 * nums[j]) + 1 from fenwick tree (log n)
        - insert each element into fenwick tree (maybe coordinate compression)

        brute force: 
        for j in range(n):
            for i in range(j):
                if nums[i] > 2 * nums[j]:
                    count += 1
        

        '''
        values = sorted(set(nums))
        rank = {
            val: i + 1
            for i, val in enumerate(values)
        }
        fenwick = FenwickTree(len(nums))
        count = 0 
        for j, num in enumerate(nums): 
            idx = bisect_right(values, 2 * nums[j])
            count_lte = fenwick.query(idx)
            count += j - count_lte
            fenwick.update(rank[nums[j]], 1)
        return count

        