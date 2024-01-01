class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        
        for char in s:
            if char not in map:
                stack.append(char)
                continue
            if not stack or stack[-1] != map[char]:
                return False
            stack.pop()
        
        return not stack