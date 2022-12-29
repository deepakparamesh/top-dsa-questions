class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k
        
        def quickselect(l,r):
            pivot, pointer = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[pointer], nums[r] = nums[r], nums[pointer]
            
            if pointer > k: return quickselect(l, pointer-1)
            elif pointer < k: return quickselect(pointer+1, r)
            else: return nums[pointer]
            
        return quickselect(0, len(nums) - 1)