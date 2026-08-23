class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive 
        self.mapping = {}      

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.mapping[tokenId] = currentTime + self.ttl
    
    def _is_expired(self, tokenId, curr_time): 
        return self.mapping[tokenId] < curr_time

    def _is_valid(self, tokenId, curr_time): 
        return tokenId in self.mapping and self.mapping[tokenId] > curr_time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.mapping or not self._is_valid(tokenId, currentTime):
            return 
        
        self.mapping[tokenId] = currentTime + self.ttl      

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0 
        for token_id in self.mapping.keys(): 
            if self._is_valid(token_id, currentTime): 
                count += 1
        return count

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)