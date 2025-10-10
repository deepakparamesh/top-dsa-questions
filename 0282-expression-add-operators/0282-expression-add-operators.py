class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
            if not num:
                return []
            
            results = []
            
            def backtrack(index, path, value, prev_operand):
                """
                Backtrack through all possible operator placements
                
                Args:
                    index: Current position in num string
                    path: Current expression being built
                    value: Current evaluated value of expression
                    prev_operand: Previous operand (needed for multiplication)
                """
                # Base case: reached end of string
                if index == len(num):
                    if value == target:
                        results.append(path)
                    return
                
                # Try all possible numbers starting from current index
                for i in range(index, len(num)):
                    # Extract current number string
                    curr_str = num[index:i+1]
                    
                    # Skip numbers with leading zeros (except "0" itself)
                    if len(curr_str) > 1 and curr_str[0] == '0':
                        break
                    
                    curr_num = int(curr_str)
                    
                    # If this is the first number (no operators yet)
                    if index == 0:
                        backtrack(i + 1, curr_str, curr_num, curr_num)
                    else:
                        # Try addition
                        backtrack(i + 1, 
                                path + '+' + curr_str, 
                                value + curr_num, 
                                curr_num)
                        
                        # Try subtraction
                        backtrack(i + 1, 
                                path + '-' + curr_str, 
                                value - curr_num, 
                                -curr_num)
                        
                        # Try multiplication (need to undo last operation)
                        backtrack(i + 1, 
                                path + '*' + curr_str, 
                                value - prev_operand + prev_operand * curr_num, 
                                prev_operand * curr_num)
            
            backtrack(0, "", 0, 0)
            return results