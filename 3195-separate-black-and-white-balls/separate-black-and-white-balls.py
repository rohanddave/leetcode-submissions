class Solution:
    def minimumSteps(self, s: str) -> int:
        '''
        problem:
        1 = black and 0 = white

        goal: return min steps to group all 1's to right

        observations: 
        - moving all black to the right end means all white will be on the left end 
        - each move means swapping adjacent balls 
        - minimum number of swaps would be if we encounter a black ball and move to just before the right pointer 
        
        approach: 
        - maintain left and right pointers 
        - while l < r 

        '''
        
        l, r = 0, len(s) - 1
        moves = 0
        while l < r: 
            while l < r and s[r] == '1': 
                r -= 1
            while l < r and s[l] == '0':
                l += 1
            
            if l < r: 
                moves += r - l 
                l += 1
                r -= 1
        return moves
 

