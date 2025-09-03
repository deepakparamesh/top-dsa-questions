class Solution:
    def calculate(self, s: str) -> int:

        def helper(index):
            """
            Helper function that processes the string starting from index.
            Returns (result, new_index) where new_index is position after processing.
            """
            stack = []
            number = 0
            operation = '+'  # Default operation for first number
            
            while index < len(s):
                char = s[index]
                
                # Build number digit by digit
                if char.isdigit():
                    number = number * 10 + int(char)
                
                # Handle opening parenthesis - recursive call
                elif char == '(':
                    number, index = helper(index + 1)
                
                # Process operation or end of expression
                if char in '+-*/)' or index == len(s) - 1:
                    # Apply the previous operation
                    if operation == '+':
                        stack.append(number)
                    elif operation == '-':
                        stack.append(-number)
                    elif operation == '*':
                        stack.append(stack.pop() * number)
                    elif operation == '/':
                        # Handle division with truncation towards zero
                        last = stack.pop()
                        if last < 0:
                            stack.append(-(-last // number))
                        else:
                            stack.append(last // number)
                    
                    # Reset for next number
                    number = 0
                    operation = char
                    
                    # Handle closing parenthesis - return result
                    if char == ')':
                        break
                
                index += 1
            
            return sum(stack), index
    
        # Remove all spaces for easier processing
        s = s.replace(' ', '')
        result, _ = helper(0)
        return result        