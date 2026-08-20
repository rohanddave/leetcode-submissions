class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        '''
        example: 
        nums = [1, 2, 3, 4, 5]
        cost = [100, 25, 25, 25, 26]

        so greedily choosing the number with highest cost and trying to make that number will give the wrong answer. greedy in this case fails 

        cost to make nums[i] equal target = abs(target - nums[i]) * cost[i] = xi
        minimize sum(xi)
        - 
        '''
        zipped = sorted(zip(nums, cost))

        def get_cost(target): 
            c = 0
            for i, (num, num_cost) in enumerate(zipped):
                c += abs(target - num) * num_cost
            return c

        l, r = zipped[0][0], zipped[-1][0]

        while l < r: 
            m = (l + r) // 2

            if  get_cost(m) > get_cost(m + 1):
                l = m + 1
            else:
                r = m
        return get_cost(l)

