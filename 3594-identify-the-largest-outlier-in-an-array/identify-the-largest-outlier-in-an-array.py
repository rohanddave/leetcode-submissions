class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        '''
        sum of array = S 
        outlier = O 
        remaining sum = S - O 
        looking for a number == (S - O) / 2
        '''
        total_sum = sum(nums) 
        counter = collections.Counter(nums)
        res = float('-inf')

        for outlier in nums: 
            target = (total_sum - outlier) / 2 # this has to be even 
            counter[outlier] -= 1
            if target in counter and counter[target] > 0:
                res = max(res, outlier)
            counter[outlier] += 1
        return res