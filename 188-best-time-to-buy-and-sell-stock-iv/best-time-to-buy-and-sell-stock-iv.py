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
        
        optimization: 
        - do we need sells and buys both? since a stock can be sold only if holding, sell will never be greater than buy. so buy can be at most sell + 1 or equal to sell 
        so if holding: buy = sell + 1
        if not holding: buy = sell
        '''
        memo = {}
        def dfs(i, holding, sells): 
            if i == len(prices): 
                return 0
            if (i, holding, sells) in memo:
                return memo[(i, holding, sells)]

            res = float('-inf')
            skip = dfs(i + 1, holding, sells)
            buy = sell = float('-inf')

            buys = sells + 1 if holding else sells
            if not holding and buys < k:
                buy = -prices[i] + dfs(i + 1, True, sells)
            if holding and sells < k: 
                sell = prices[i] + dfs(i + 1, False, sells + 1)
            
            memo[(i, holding, sells)] = max(skip, buy, sell)
            return memo[(i, holding, sells)]
        return dfs(0, False, 0)
            
