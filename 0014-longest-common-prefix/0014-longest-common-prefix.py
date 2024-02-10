class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for index in range(len(strs[0])):
            for s in strs:
                if index == len(s) or s[index] != strs[0][index]:
                    return result
            result += strs[0][index]
            
        return result
            