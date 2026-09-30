class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []
        for i, num in enumerate(nums): 
            if num != 0:
                self.nums.append((i, num))     

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0 
        i, j = 0, 0 
        while i < len(self.nums) and j < len(vec.nums): 
            if self.nums[i][0] < vec.nums[j][0]:
                i += 1
            elif self.nums[i][0] > vec.nums[j][0]:
                j += 1
            else: 
                res += self.nums[i][1] * vec.nums[j][1]
                i += 1
                j += 1
        return res      
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)