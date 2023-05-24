class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
      # if the length of two words are unequal, you can return false
        
      #  loop through s 
      #   check if the character is availabe in the t,
            # if True -> remove the character
            # if False -> return false
      # if it reaches the end of the loop, return True
      
      if len(s) != len(t):
        return False
      
      sMap, tMap = {} , {}
      
      for i in range(len(s)):
        sMap[s[i]] = 1+ sMap.get(s[i],0)
        tMap[t[i]] = 1+ tMap.get(t[i],0)
      
      return sMap == tMap