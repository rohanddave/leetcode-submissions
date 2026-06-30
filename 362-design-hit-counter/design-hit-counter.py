class HitCounter:

    def __init__(self):
        self.window = collections.deque()        

    def hit(self, timestamp: int) -> None:
        self.window.append(timestamp)       

    def getHits(self, timestamp: int) -> int:
        target = timestamp - 299

        left, right = 0, len(self.window)
        while left < right:
            m = (left + right) // 2

            if self.window[m] >= target:
                right = m
            else:
                left = m + 1
        return len(self.window) - left





# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)