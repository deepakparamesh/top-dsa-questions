class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        max_so_far = nums[0]
        max_ending_here = nums[0]
        min_ending_here = nums[0]

        for i in range(1, len(nums)):
            current=nums[i]

            temp_max = max(current, max_ending_here * current, min_ending_here * current)

            min_ending_here = min(current, max_ending_here* current, min_ending_here*current)

            max_ending_here = temp_max

            max_so_far = max(max_so_far, max_ending_here)
    
        return max_so_far




# 0: num = 2
# [2,3,-2,4]
# max=2
# min=2
# global_max=2

# 1: num=3
# max = max(3,2*3) = 6
# min = min(3,2*3)= 3
# global_max = 6
# 2 : -2
# max = max(-2,6*(-2),3*(-2)) = -2
# min = min(-2, 6*-2, 3*-2)=-12
# global_max = 6