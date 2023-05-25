class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
          return False
        
        sCount,tCount = {},{}
        
        for i in range(len(s)):
          sCount[s[i]] = 1+sCount.get(s[i],0)
          tCount[t[i]] = 1+tCount.get(t[i],0)
        
        return tCount == sCount