class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        '''
        goal: return len of shortest non empty subarray with sum >= k. return -1 if none 

        observations: 
        - numbers could be negative so sliding window will not work 
        - prefix[j] - prefix[i] >= k means there exists subarray from j to i with sum >= k
        - for index j we need the earliest i that makes the sum >= k 
        - if the sum was exactly k then a prefix + hashmap would work since we could just look for prefix[j] - k
        - let's say we use an i with a j to form a subarray all the indices before i are useless for future computations because the length of subarray would only be longer. this indicates we need a mono deque of prefix sums

        approach: 
        - 
        '''
        prefix = [0] 
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        dq = collections.deque()        
        ans = float('inf')

        for j in range(len(prefix)):
            while dq and prefix[j] - prefix[dq[0]] >= k:
                ans = min(ans, j - dq.popleft())
            
            while dq and prefix[dq[-1]] >= prefix[j]:
                dq.pop()
            
            dq.append(j)
        return -1 if ans == float('inf') else ans

        