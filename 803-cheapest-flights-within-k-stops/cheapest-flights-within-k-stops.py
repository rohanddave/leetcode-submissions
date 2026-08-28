class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        min_cost = [float('inf')] * n 
        min_cost[src] = 0

        for _ in range(k + 1):
            temp = min_cost.copy() 
            for u, v, w in flights:
                temp[v] = min(temp[v], min_cost[u] + w)
            min_cost = temp 
        res = min_cost[dst] 
        return res if res != float('inf') else -1
            



        