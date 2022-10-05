# How do I detect the last word first, The delimiter is Space.
# Instead of going from the front to back, we can count from the last of the array.
# When we hit the first space, then we have detected a word. return the number of count that we have used.
# edge case is : if there is any space at the end of the word.
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