class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(number):
            totalSum = 0
            
            while number > 0:
                digit = number % 10
                totalSum += digit ** 2
                number //= 10
            return totalSum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
    