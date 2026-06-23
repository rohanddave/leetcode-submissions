class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = [] 
        prev_smaller = [-1] * n 

        for i in range(n): 
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack: 
                prev_smaller[i] = stack[-1]
            
            stack.append(i)
        
        stack = [] 
        next_smaller = [n] * n 
        
        for i in range(n - 1, -1, -1): 
            while stack and heights[stack[-1]] >= heights[i]: 
                stack.pop()
            
            if stack: 
                next_smaller[i] = stack[-1]
            
            stack.append(i)
        
        ans = 0

        for i in range(n): 
            left_wall = prev_smaller[i] + 1
            right_wall = next_smaller[i] - 1
            width = right_wall - left_wall + 1
            area = heights[i] * width 
            ans = max(ans, area)
        
        return ans