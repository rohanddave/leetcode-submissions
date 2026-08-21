class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        '''
        problem:
        - maximum sum along fixed size window of length minutes 

        max satisfied = already satisfied + max(extra)

        approach: 
        - calculate the already satisfied count
        - a fixed window of size minutes 
        - maintain extra satisfied count for window 
        - track the maximum value of extra satisfied across all windows 
        - return already satisfied + max extra satisfied
        '''
        n = len(customers)

        # calculate already satisfied
        already_satisfied = 0 
        for i in range(n):
            if grumpy[i] == 0: 
                already_satisfied += customers[i]
        
        max_extra = float('-inf')
        window_extra = 0 
        l = 0
        for r in range(n):
            if grumpy[r] == 1:
                window_extra += customers[r]
            
            if r < minutes - 1:
                continue
            
            max_extra = max(max_extra, window_extra)
            if grumpy[l] == 1: 
                window_extra -= customers[l]
            l += 1
            
        return already_satisfied + max_extra
        