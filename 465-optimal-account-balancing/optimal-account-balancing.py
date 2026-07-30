class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        '''
        problem: 
        - transactions[i] = [from, to, amount] 
        
        goal: return min number of transactions to settle debt 

        example: 
        Input: transactions = [[0,1,10],[2,0,5]]
        Output: 2

        0 -> 1 = 10 
        2 -> 0 = 5

        0: -5 
        1: +10
        2: -5
        ------

        0: -4
        1: 4
        2: 0

        observations: 
        - we need each person's balance to be 0
        - we have:
            - people that need to receive money (-ve)
            - people that need to send money (+ve )
            - neither need to receive or send money (0)
        
        approach:
        for each person that needs to send money:
            try to send money to every person person that needs to receive amount <= surplus current person has 
        
        state: 
        - 
        '''
        net = collections.defaultdict(int)
        for from_id, to_id, amt in transactions:
            net[from_id] -= amt # -ve balance means this person is owed money
            net[to_id] += amt # +ve balance means this person needs to pay money
        
        balances = [val for val in net.values() if val != 0]
        # i index is for each positve balance which should be paired with a negative j index

        # +5, -10
        def dfs(i):
            while i < len(balances) and balances[i] == 0:
                i += 1
            
            if i == len(balances): 
                return 0

            count = float('inf')
            for j in range(i + 1, len(balances)):
                # if opposite signs and neither is 0
                if balances[j] * balances[i] < 0:
                    original_i, original_j = balances[i], balances[j]

                    transfer = min(abs(balances[i]), abs(balances[j]))
                    if balances[i] < 0: 
                        balances[i] += transfer
                        balances[j] -= transfer
                    else:
                        balances[i] -= transfer
                        balances[j] += transfer
                    
                    count = min(count, 1 + dfs(i + 1 if balances[i] == 0 else i))
                    balances[i], balances[j] = original_i, original_j
            return count

        return dfs(0)