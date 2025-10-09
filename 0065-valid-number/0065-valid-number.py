class Solution:
    def isNumber(self,s: str) -> bool:
        """
        Validates if a string represents a valid number.
        
        A valid number can be:
        1. An integer (with optional sign)
        2. A decimal (with optional sign)
        3. Either of above with an exponent part
        """
        
        def is_integer(num_str):
            """
            Helper function to check if a string is a valid integer.
            Valid integers: "123", "+123", "-123"
            """
            if not num_str:  # Empty string is not valid
                return False
            
            # Remove optional sign from beginning
            if num_str[0] in ['+', '-']:
                num_str = num_str[1:]
            
            # After removing sign, must have at least one digit
            if not num_str:
                return False
            
            # Check if all remaining characters are digits
            return num_str.isdigit()
        
        def is_decimal(num_str):
            """
            Helper function to check if a string is a valid decimal.
            Valid decimals: "3.14", ".5", "46.", "+.5", "-46."
            """
            if not num_str:  # Empty string is not valid
                return False
            
            # Remove optional sign from beginning
            if num_str[0] in ['+', '-']:
                num_str = num_str[1:]
            
            # After removing sign, must have content
            if not num_str:
                return False
            
            # Check if it's just digits (integer without decimal point)
            if num_str.isdigit():
                return True
            
            # Split by decimal point
            if '.' in num_str:
                parts = num_str.split('.')
                
                # Must have exactly one decimal point
                if len(parts) != 2:
                    return False
                
                before_decimal, after_decimal = parts
                
                # At least one part must have digits
                # Both parts (if present) must contain only digits
                has_digits = False
                
                if before_decimal:
                    if not before_decimal.isdigit():
                        return False
                    has_digits = True
                
                if after_decimal:
                    if not after_decimal.isdigit():
                        return False
                    has_digits = True
                
                return has_digits
            
            return False
        
        # Main validation logic
        if not s:  # Empty string is not valid
            return False
        
        # Convert to lowercase for easier 'e' detection
        s_lower = s.lower()
        
        # Find the position of 'e' (if exists)
        e_index = -1
        for i, char in enumerate(s_lower):
            if char == 'e':
                e_index = i
                break
        
        # Split into base and exponent parts
        if e_index != -1:
            # Has exponent
            base_part = s[:e_index]
            exp_part = s[e_index + 1:]
            
            # Both parts must be valid
            # Base can be integer or decimal
            # Exponent must be integer
            return (is_integer(base_part) or is_decimal(base_part)) and is_integer(exp_part)
        else:
            # No exponent, just check if it's a valid integer or decimal
            return is_integer(s) or is_decimal(s)

        