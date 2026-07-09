class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        '''
        goal: return min k-bit flips so that no 0 in array. if not possible return -1

        problem:
        - array contains only 0's and 1's 
        - k bit flip = subarray of length k, every 0 -> 1 and every 1 -> 0
        
        observations: 
        - we only care about the current start of the window because the other k - 1 elements can potentially be switched again in a future window 
        - so we perform a k bit flip only when the left pointer element is a 0
        - 
        - optimization would be to avoid rescanning the entire window to perform the flips
        - we need to know the number of flips of current index 
            - if parity[i] % 2 == 0 then final[i] = nums[i]
            - else final[i] = !nums[i]

        example: 
        Input: nums = [0,1,0], k = 1
        Output: 2

        Input: nums = [1,1,0], k = 2
        Output: -1

        Input: nums = [0,0,0,1,0,1,1,0], k = 3
        Output: 3

        '''
        n = len(nums)
        started = [False] * n
        active = 0 
        ans = 0

        def final(i, flips):
            return nums[i] if flips % 2 == 0 else (1 if nums[i] == 0 else 0)

        for i in range(n):
            if i >= k:
                active -= 1 if started[i - k] else 0

            if final(i, active) == 0: 
                if i + k > n:
                    return -1
                started[i] = True
                active += 1
                ans += 1

        return ans
            

        