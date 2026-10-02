class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        '''
        problem: 
        - orders[i] = [price, amount, orderType]
        - orderType = 0 (buy) or orderType = 1 (sell)
        - order[i] comes before order[i + 1] (left to right sweep)
        - matching (if order matched not entered in backlog): 
            - buy order matches with smallest price in sell backlog (sell in min heap by price) 
            - sell order matches with largest price in buy backlog (buy in max heap by price)
        '''
        BUY, SELL = 0, 1

        # heap stores (price, qty)
        buy_heap = [] # max heap by price 
        buy_heap_size = 0
        sell_heap = [] # min heap by price 
        sell_heap_size = 0

        for price, amount, orderType in orders: 
            # insert into respective heap
            if orderType == BUY:
                heapq.heappush(buy_heap, (-price, amount))
                buy_heap_size += amount
            else: 
                heapq.heappush(sell_heap, (price, amount))
                sell_heap_size += amount
            
            while buy_heap and sell_heap and -buy_heap[0][0] >= sell_heap[0][0]:
                neg_buy_price, buy_amount = heapq.heappop(buy_heap)
                sell_price, sell_amount = heapq.heappop(sell_heap)

                matched_amount = min(buy_amount, sell_amount)
                buy_heap_size -= matched_amount
                sell_heap_size -= matched_amount

                if buy_amount == sell_amount:
                    continue
                elif buy_amount < sell_amount: 
                    amount = sell_amount - buy_amount
                    heapq.heappush(sell_heap, (sell_price, amount))
                else:
                    amount = buy_amount - sell_amount
                    heapq.heappush(buy_heap, (neg_buy_price, amount))
            

        
        return(buy_heap_size + sell_heap_size) % (10 **9 + 7)
