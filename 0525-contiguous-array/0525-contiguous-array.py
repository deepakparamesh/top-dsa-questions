class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        count = 0
        max_length = 0
        count_dict = { 0 : -1}
        
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else: 
                count -=1 
                
            
            if count in count_dict:
                max_length = max(max_length, i - count_dict[count])
            else:
                count_dict[count] = i
            
        return max_length
                
 

# [0,1,0]
#    i

# count = 0
# MAXLength = 0
# -1 : 0
#  0 : -1
