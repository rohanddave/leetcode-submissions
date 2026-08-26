class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        '''
        goal: return maximum difference between successive elements in sorted form in linear time and linear space 

        observations:
        - since linear time requirement cannot actually sort array 
        - explore non comparision based sorting techniques like bucket or cyclic sort
        - duplicate numbers are possible
        - numbers are in the range [min(nums), max(nums)]
        - there are n - 1 gaps
        - gap size is in the range [0, max(nums) - min(nums) // (n - 1)]
        
        example:
        Input: nums = [3,6,9,1]
        Output: 3

        sorted order = [1, 3, 6, 9]
        max(3 - 1, 6 - 3, 9 - 6) = 3

        gaps = [[], [], []]

        approach: 
        - create buckets array of length max(nums) + 1: indices are from [0, max(nums)]
        - place each number at bucket[num] (we don't need to store duplicates)
        - go through the  buckets maintaining a prev non empty and for each current non empty store the difference in a result max
        - this approach needs max(nums) number of buckets 

        optimization: 
        - 
        '''
        n = len(nums)

        if n < 2: 
            return 0

        mn, mx = min(nums), max(nums)

        if mn == mx:
            return 0

        avg_bucket_size = math.ceil((mx - mn)/(n - 1))
        number_of_buckets = (mx - mn) // avg_bucket_size + 1
        bucket_min = [float('inf')] * number_of_buckets
        bucket_max = [float('-inf')] * number_of_buckets

        for i, num in enumerate(nums):
            bucket_idx = (num - mn) // avg_bucket_size
            bucket_min[bucket_idx] = min(bucket_min[bucket_idx], num)
            bucket_max[bucket_idx] = max(bucket_max[bucket_idx], num)
        
        res = 0 
        prev_max = None
        for i in range(number_of_buckets): 
            if bucket_min[i] == float('inf'):
                continue
            if prev_max is not None:
                res = max(res, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return res
            

        