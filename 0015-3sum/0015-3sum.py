class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for index, value in enumerate(nums):
            
            if value > 0:
                break
            
            if index > 0 and value == nums[index-1]:
                continue
            
            left = index+1
            right = len(nums)-1
            
            while left < right:
                currentSum = nums[index] + nums[left] + nums[right]
                if currentSum == 0:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                elif currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left += 1
            
        return result