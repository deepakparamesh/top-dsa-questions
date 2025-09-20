class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Define 32-bit integer bounds
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Handle empty string
        if not s:
            return 0
        
        # Initialize variables
        index = 0
        n = len(s)
        result = 0
        sign = 1  # 1 for positive, -1 for negative
        
        # Step 1: Skip leading whitespace
        while index < n and s[index] == ' ':
            index += 1
        
        # Check if we've reached the end after skipping spaces
        if index >= n:
            return 0
        
        # Step 2: Check for sign
        if s[index] == '+':
            sign = 1
            index += 1
        elif s[index] == '-':
            sign = -1
            index += 1
        
        # Step 3: Process digits
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            # Check for overflow BEFORE multiplication
            # If result > INT_MAX // 10, then result * 10 would overflow
            # If result == INT_MAX // 10, then we need to check the last digit
            if result > INT_MAX // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            if result == INT_MAX // 10:
                # For positive: if last digit > 7, it would overflow (2147483647)
                # For negative: if last digit > 8, it would overflow (-2147483648)
                if sign == 1 and digit > 7:
                    return INT_MAX
                if sign == -1 and digit > 8:
                    return INT_MIN
            
            # Safe to add the digit
            result = result * 10 + digit
            index += 1
        
        # Step 4: Apply sign and return
        return sign * result





