class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
        
#         wordLength = 0;
        
#         for i in s[::-1]:
#             if i == " ":
#                 if wordLength >= 1:
#                     return wordLength
#             else:
#                 wordLength +=1
        
#         return wordLength
    
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s)-1, 0
        
        while s[i] == " ":
            i -= 1;
        while i >= 0 and s[i] != " ":
            length +=1
            i -= 1
        
        return length