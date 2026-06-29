class MovingAverage:

    def __init__(self, size: int):
        self.window = collections.deque()
        self.left = 0 
        self.right = -1
        self.curr_sum = 0
        self.max_size = size
        '''
        size = 3
        nums = [1, 2, 3, 4]
        '''
        

    def next(self, val: int) -> float:
        self.window.append(val) 
        self.curr_sum += val 
        self.right += 1

        window_size = self.right - self.left + 1
        if window_size > self.max_size:
            self.curr_sum -= self.window.popleft()
            self.left += 1
        return self.curr_sum / len(self.window)



        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)