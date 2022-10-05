class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        wordLength = 0;
        
        for i in s[::-1]:
            if i == " ":
                if wordLength >= 1:
                    return wordLength
            else:
                wordLength +=1
        
        return wordLength