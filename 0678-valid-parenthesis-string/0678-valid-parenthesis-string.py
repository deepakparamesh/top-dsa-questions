class Solution:
    def checkValidString(self, s: str) -> bool:
        open_min = 0  # Minimum number of open parentheses
        open_max = 0  # Maximum number of open parentheses

        for char in s:
            if char == '(':
                open_min += 1
                open_max += 1
            elif char == ')':
                open_min -= 1
                open_max -= 1
            elif char == '*':
                open_min -= 1
                open_max += 1

            if open_max < 0:
                return False
            if open_min < 0:
                open_min = 0

        return open_min == 0
        
        