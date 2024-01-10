class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        charSet = set()
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left +=1
            charSet.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest
