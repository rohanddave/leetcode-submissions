class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        goal: return max profit 

        problem: 
        - prices[i] = price of stock on ith day 
        - fee = transaction fee
        - infinite transactions, but need to pay transaction fee for a transaction 
        - can hold only one stock at a time 
        - transaction fee charged for a buy and sell pair 

        state: 
        - i = current day 
        - holding = if holding stock or not 

        observation: 
        - charge transaction fee when selling because we can only sell after buying and transaction fee is charged after selling

        approach: 
        - dynamic programming 
        - on each day: 
            - skip
            - buy if not holding
            - sell if holding
        '''
        memo = {}
        def dfs(i, holding): 
            if i == len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            buy = sell = float('-inf')
            skip = dfs(i + 1, holding)
            if not holding: 
                buy = -prices[i] + dfs(i + 1, True)
            else: 
                sell = prices[i] - fee + dfs(i + 1, False)
            memo[(i, holding)] = max(buy, sell, skip)
            return memo[(i, holding)]
        return dfs(0, False)
        