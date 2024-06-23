class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        start, end = 0, 0

        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindromes
            left1, right1 = expand_around_center(s, i, i)
            # Even length palindromes
            left2, right2 = expand_around_center(s, i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end+1]