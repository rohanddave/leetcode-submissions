class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        goal: max profit with buying at most k times and selling at most k times 

        problem: 
        - prices[i] = price of stock on ith day 
        - must sell stock before buying again 

        observation:
        - we're allowed to buy k times 
        - we're allowed to sell k times 
        - if we're holding stock we cannot buy again 
        - if we're not holding stock we cannot sell 
        - we can choose to skip a day (holding or not holding)
        
        approach: 
        - dynamic programming 
        - on the ith day
            - buy if not holding already and if number of buys <= k
            - sell if holding and number of sells <= k 
            - skip 
        - dfs(i, number_of_buys, number_of_sells) returns the maximum profit possible from the ith day given number_of_buys and number_of_sells up until ith day
        '''
        memo = {}
        def dfs(i, holding, buys, sells): 
            if i == len(prices): 
                return 0
            if (i, holding, buys, sells) in memo:
                return memo[(i, holding, buys, sells)]

            res = float('-inf')
            skip = dfs(i + 1, holding, buys, sells)
            buy = sell = float('-inf')
            if not holding and buys < k:
                buy = -prices[i] + dfs(i + 1, True, buys + 1, sells)
            if holding and sells < k: 
                sell = prices[i] + dfs(i + 1, False, buys, sells + 1)
            
            memo[(i, holding, buys, sells)] = max(skip, buy, sell)
            return memo[(i, holding, buys, sells)]
        return dfs(0, False, 0, 0)
            
