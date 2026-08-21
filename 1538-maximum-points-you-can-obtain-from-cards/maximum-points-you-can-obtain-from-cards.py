class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        problem: 
        - pick begining or end 
        - take exactly k cards
        - score = sum of picked cards 
        
        goal: return max score by picking k cards 

        observations: 
        - greedy is tempting i.e. pick the largest of the begining and end but this will not give a global optimal answer 
        

        approach: 
        - dynamic programming i.e. at each step pick begining and end return max
        '''
        
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        l, window_sum = 0, 0
        min_window_sum = float('inf')
        for r in range(n): 
            window_sum += cardPoints[r]

            if r - l + 1 < n - k:
                continue
            
            min_window_sum = min(min_window_sum, window_sum)
            window_sum -= cardPoints[l]
            l += 1
        
        return sum(cardPoints) - min_window_sum

            
        