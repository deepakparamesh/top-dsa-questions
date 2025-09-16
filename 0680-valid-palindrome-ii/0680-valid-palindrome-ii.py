class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        More verbose version for better understanding.
        """
        n = len(s)
        
        # Edge cases
        if n <= 2:
            return True
        
        # Find first mismatch
        left, right = 0, n - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        
        # If no mismatch, already palindrome
        if left >= right:
            return True
        
        # Helper to check palindrome
        def check_palindrome(string):
            return string == string[::-1]
        
        # Try removing character at left pointer
        option1 = s[:left] + s[left+1:]
        if check_palindrome(option1):
            return True
        
        # Try removing character at right pointer
        option2 = s[:right] + s[right+1:]
        if check_palindrome(option2):
            return True
        
        return False