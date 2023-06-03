class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for index, num in enumerate(nums):
          if num > 0:
            break
          if index > 0 and num == nums[index-1]:
            continue
          left, right = index + 1, len(nums) - 1
          
          while left < right:
            threesum = nums[left]+nums[right]+num
            if threesum < 0:
              left +=1
            elif threesum > 0:
              right -=1
            else:
              result.append([num, nums[left], nums[right]])
              left +=1
              while nums[left] == nums[left-1] and left < right:
                left +=1
        
        return result
              
  