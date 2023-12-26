class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ''
        for char in s:
            if char.isalpha() or char.isdigit():
                formatted += char.lower()
        
        return (formatted == formatted[::-1])
            