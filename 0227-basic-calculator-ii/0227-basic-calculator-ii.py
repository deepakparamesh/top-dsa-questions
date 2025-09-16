class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []  # Stack to store numbers for final addition/subtraction
        current_number = 0  # Current number being parsed
        operation = '+'  # Previous operation (start with '+' for first number)
        
        # Process each character in the expression
        for i, char in enumerate(s):
            
            # Build multi-digit numbers
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            # When we hit an operator or reach end of string, process the current number
            if char in '+-*/' or i == len(s) - 1:
                
                if operation == '+':
                    # Addition: push positive number to stack
                    stack.append(current_number)
                    
                elif operation == '-':
                    # Subtraction: push negative number to stack  
                    stack.append(-current_number)
                    
                elif operation == '*':
                    # Multiplication: pop last number, multiply, push result back
                    last_number = stack.pop()
                    stack.append(last_number * current_number)
                    
                elif operation == '/':
                    # Division: pop last number, divide with truncation toward zero
                    last_number = stack.pop()
                    # Python's // operator truncates toward negative infinity
                    # We need truncation toward zero, so handle negative case
                    if last_number < 0:
                        # For negative numbers, use ceiling division toward zero
                        result = -(-last_number // current_number)
                    else:
                        # For positive numbers, normal floor division
                        result = last_number // current_number
                    stack.append(result)
                
                # Reset for next number and update operation
                current_number = 0
                if char in '+-*/':  # Don't update operation at end of string
                    operation = char
        
        # Sum all numbers in stack (handles deferred addition/subtraction)
        return sum(stack)