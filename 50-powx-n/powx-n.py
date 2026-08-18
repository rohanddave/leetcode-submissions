class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        def helper(x, n): 
            if n == 0:
                return 1
            if n == 1: 
                return x 
            half = helper(x, n // 2)
            return half * half * (x if n % 2 != 0 else 1)
        
        res = helper(x, abs(n) // 2)
        res = res * res 
        res = res * x if n % 2 != 0 else res
        return 1/res if n < 0 else res