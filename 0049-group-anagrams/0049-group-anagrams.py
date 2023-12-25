class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        anagramDictionary = {}
        
        for str in strs:
            hashcode = [0] * 26
            
            for char in str:
                hashcode[ord(char) - ord('a')] += 1
            
            if tuple(hashcode) not in anagramDictionary :
                anagramDictionary[tuple(hashcode)] = []
                
            anagramDictionary[tuple(hashcode)].append(str)    
        
        return anagramDictionary.values()
    
                
        