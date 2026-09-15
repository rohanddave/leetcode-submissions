class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = [] 
        answer = [price for price in prices]
        for i in range(n - 1, -1, -1): 
            while stack and prices[stack[-1]] > prices[i]: 
                stack.pop()
            
            if stack: 
                answer[i] -= prices[stack[-1]]

            stack.append(i)
        return answer

        