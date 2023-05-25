class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare a key value with value as array
        result = collections.defaultdict(list)
        
        for string in strs:
          countHolder = [0]*26
          for character in string:
            # 101 - 97 = 4
            countHolder[ord(character) - ord('a')] += 1
          result[tuple(countHolder)].append(string)
        
        return result.values()