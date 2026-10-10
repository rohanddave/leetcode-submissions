class Leaderboard:

    def __init__(self):
        self.mapping = collections.defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.mapping[playerId] += score        

    def top(self, K: int) -> int:
        heap = []
        for playerId, score in self.mapping.items(): 
            heapq.heappush(heap, score)
            if len(heap) > K: 
                heapq.heappop(heap)
        
        return sum(heap)
        

    def reset(self, playerId: int) -> None:
        del self.mapping[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)