class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if x == 0.0:
            return 0.0
        
        if n < 0:
            return 1.0/self.myPow(x,-n)
        
        result = 1.0
        base = x

        while n > 0:

            if n & 1:
                result *= base
            
            base *= base

            n >>= 1
        
        return result

        # x^n = (x^(n/2))^2
        # x^n =  x * (x^((n-1)/2))^2