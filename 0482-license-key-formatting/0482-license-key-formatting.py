class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        cleaned = []
        for char in s:
            if char != '-':
                cleaned.append(char.upper())
        
        
        total_length = len(cleaned)
        first_group_length = total_length % k if total_length % k != 0 else k
        
        result = []
        i = 0
        result.append(''.join(cleaned[i: first_group_length + i]))
        i += first_group_length
        
        while i < total_length:
            result.append(''.join(cleaned[i:i+k]))
            i += k
    
        return '-'.join(result)