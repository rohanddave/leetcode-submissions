class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        '''
        goal: return the max amt of coins by collecting k consecutive bags 

        observations: 
        - segment of coins are non overlapping 
        
        
        approach:
        - fixed size sliding window of size k 
        - we include an entire interval or partial interval when expanding the window 
        - how do we shrink the window tho?
        '''
        coins.sort() 

        def sweep(intervals):
            window_count = 0
            max_coins = 0
            j = 0

            for i in range(len(intervals)): 
                left = intervals[i][0]
                right = left + k - 1

                while j < len(intervals) and intervals[j][1] <= right:
                    l, r, count = intervals[j]
                    window_count += (r - l + 1) * count
                    j += 1                
                
                total = window_count 
                if j < len(intervals):
                    l, r, count = intervals[j] 
                    overlap = max(0, right - l + 1)
                    total += overlap * count
                
                max_coins = max(max_coins, total)

                l, r, count = intervals[i] 
                window_count -= (r - l + 1) * count
            
            return max_coins 
        
        # Reverse intervals so the second sweep aligns the window's
        # right boundary with interval ends.
        rev = []
        for l, r, c in reversed(coins):
            rev.append([-r, -l, c])
        
        ans = max(sweep(coins), sweep(rev))

        return ans
            

            
            


