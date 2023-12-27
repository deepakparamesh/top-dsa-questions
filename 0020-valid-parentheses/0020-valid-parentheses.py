class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        bracketMap ={
            "}":"{",
            ")":"(",
            "]":"["
        }
        
        for char in s:
            if char not in bracketMap:
                stack.append(char)
                continue
            if not stack or stack[-1] != bracketMap[char]:
                return False
            stack.pop()
            
        if(len(stack) == 0):
            return True
        else:
            return False
