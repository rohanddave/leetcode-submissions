class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        '''
        [6,7,8,9]
        6,7,8
        6,8,9
        7,8,9

        observations: 
        - generating all triplets and calculating the running xor across 
        - like generating combinations of length 3 
        - what happens for duplicates because x ^ x = 0 and 0 ^ y = y
        '''
        n = len(nums)
        pairs = {0}

        for i in range(n):
            for j in range(i + 1, n):
                pairs.add(nums[i] ^ nums[j])
        
        res = set()
        for i in range(n):
            for xor in pairs:
                res.add(xor ^ nums[i])
        
        return len(res)

