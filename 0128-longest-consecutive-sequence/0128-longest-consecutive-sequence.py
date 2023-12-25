class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         [100,4,200,1,3,2]
        
#         [1,2,3,4,100,200]
#         O(nlogn)
#         O(1)
        
        numSet = set(nums)
        globalLongest = 0
        
        for num in nums:
            localLongest = 1
            if num-1 not in numSet:
                while num+localLongest in numSet:
                    localLongest += 1
            globalLongest = max(localLongest, globalLongest)
        
        return globalLongest
    
                
            
        