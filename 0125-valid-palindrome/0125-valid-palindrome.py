class Solution:
     # Short hand solution
#     def isPalindrome(self, s: str) -> bool:
#         formatted = ''
#         for char in s:
#             if char.isalpha() or char.isdigit():
#                 formatted += char.lower()
        
#         return (formatted == formatted[::-1])
            
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right =  len(s) - 1
        
        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            while left < right and not self.isAlphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True
    
    def isAlphaNum(self, char):
        return (
            ord('A') <= ord(char) <= ord('Z') or 
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )
