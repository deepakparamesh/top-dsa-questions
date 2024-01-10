class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        left = 0
        result = 0
        
        for right in range(len(s)):
            
            count[s[right]] = count.get(s[right],0) + 1
            
            while (right-left+1 - max(count.values())) > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right-left+1)
        return result