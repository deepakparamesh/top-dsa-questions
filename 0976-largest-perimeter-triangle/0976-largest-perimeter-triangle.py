class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        # if(nums[0] + nums[2] > nums[1]):
        #     return nums[0] + nums[1] + nums[2]
        # else:
        #     return 0
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return sum(nums[i:i+3])
        return 0