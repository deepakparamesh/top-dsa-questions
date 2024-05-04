class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for char in s[::-1]:
            if char == " ":
                if count > 0:
                    return count
            else:
                count += 1
        return count