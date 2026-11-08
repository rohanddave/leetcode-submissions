class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.arr = [-1] * n

    def allocate(self, size: int, mID: int) -> int:
        l = 0 
        gathered = 0
        for r in range(self.n): 
            window_size = r - l + 1
            if self.arr[r] == - 1:
                gathered += 1

            if window_size < size:
                continue 
            
            if gathered == size:
                break

            if self.arr[l] == -1:
                gathered -= 1
            l += 1
        
        if gathered != size:
            return -1

        for i in range(l, r + 1): 
            self.arr[i] = mID
        return l

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.arr[i] == mID:
                count += 1
                self.arr[i] = -1
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)