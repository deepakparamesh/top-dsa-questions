class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
          
          while left < right and not self.alphaNumeric(s[left]):
              left +=1
          
          while left < right and not self.alphaNumeric(s[right]):
              right -=1
          
          if s[left].lower() != s[right].lower():
              return False
          
          left +=1
          right -=1
        return True
        
        
    
    
    def alphaNumeric(self, char):
      return ( ord('a') <= ord(char) <= ord('z') or
               ord('A') <= ord(char) <= ord('Z') or
               ord("0") <= ord(char) <= ord("9"))