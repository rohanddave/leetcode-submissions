class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        problem:
        - k operations 
        - in one operation increment element at an index by 1

        goal: return max possible freq of element after performing AT MOST k operations 

        observations: 
        - nums[i] can become at most nums[i] + k
        - we never apply the operation on the largest number
        - search space is monotonic for a target (we try to get the max freq of this element)
        '''
        nums.sort()
        left, res = 0, 0
        window_sum = 0

        for right in range(len(nums)):
            target = nums[right]
            window_sum += nums[right]
            window_size = right - left + 1
            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
                
            res = max(res, right - left + 1)

        return res


        

        