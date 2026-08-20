class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        next_smaller = [n] * n
        stack = []
        for i in range(n - 1, -1, -1): 
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack: 
                next_smaller[i] = stack[-1]

            stack.append(i)
        
        stack = [] 
        prev_smaller = [-1] * n
        for i in range(n): 
            while stack and heights[stack[-1]] >= heights[i]: 
                stack.pop()
            
            if stack: 
                prev_smaller[i] = stack[-1]
            
            stack.append(i)
        
        res = float('-inf')
        for i, height in enumerate(heights): 
            l_boundary = prev_smaller[i] + 1
            r_boundary = next_smaller[i] - 1

            width = r_boundary - l_boundary + 1
            res = max(res, height * width)
            
        return res