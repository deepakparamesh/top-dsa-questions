class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        no, cnt = set(brokenLetters), 0
        for word in text.split():
            if all(c not in no for c in word):
                cnt += 1
        return cnt