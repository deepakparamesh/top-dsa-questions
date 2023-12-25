class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         [1,1,1,2,2,3] K = 2
        
#         frequencyDictionary = {
#             1:3
#             2:2
#             3:1
#         }
        
#         Timecomplexity : O(n) * O(nlogn)
#         SpaceComplexity: O(n)
            
#                   0   1   2  3  4  5   6
#         bucket = [[],[3],[2],[1],[],[],[]]
        
#         result = [1,2]
        
#         O(n) + O(n) + O(nlen(bucket)) => O(n*m)
        
        frequencyDictionary = {}
        
        for num in nums:
            frequencyDictionary[num] = frequencyDictionary.get(num, 0) + 1
        
        bucket = [[] for i in range(len(nums)+1)]
        
        for key, value in frequencyDictionary.items():
            bucket[value].append(key)
        
        result = []
        for topindex in range(len(bucket)-1,-1,-1):
                if len(bucket[topindex]) > 0:
                    for num in bucket[topindex]:
                        if len(result) < k:
                            result.append(num)
        
        return result