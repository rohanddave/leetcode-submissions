class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        '''
        goal: return string that represents the kth largest in nums (duplicates should be counted distinctly)

        observations: 
        - numbers are strings 
        - duplicates should count distinctly 

        approach: 
        approach 1:
        - quick select
        
        approach 2: 
        - min heap of size k
        '''
        # def quick_select(l, r): 
        #     pivot = r 
        #     curr = l

        #     for i in range(l, r): 
        #         if int(nums[i]) <= int(nums[pivot]): 
        #             nums[curr], nums[i] = nums[i], nums[curr]
        #             curr += 1
        #     nums[curr], nums[pivot] = nums[pivot], nums[curr]
        #     return curr 
        
        # left, right = 0, len(nums) - 1
        # k = len(nums) - k
        # while True:
        #     curr_k = quick_select(left, right) 
        #     if curr_k < k:
        #         left = curr_k + 1
        #     elif curr_k > k:
        #         right = curr_k - 1
        #     else:
        #         return nums[curr_k]

        min_heap = [] 
        for i in range(len(nums)):
            heapq.heappush(min_heap, (int(nums[i]), nums[i]))
            if len(min_heap) > k: 
                heapq.heappop(min_heap)
        return min_heap[0][1]

        