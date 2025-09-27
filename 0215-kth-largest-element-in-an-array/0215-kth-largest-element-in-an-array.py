class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]

        # def quickselect(left, right, k_smallest):

        #     if left == right:
        #         return nums[left]
            
        #     pivot_index = random.randint(left, right)

        #     pivot_index = partition(left, right, pivot_index)

        #     left_count = pivot_index - left

        #     if k_smallest <= left_count:
        #         return quickselect(left, pivot_index -1, k_smallest)
        #     elif k_smallest == left_count + 1:
        #         return nums[pivot_index]
        #     else:
        #         return quickselect(pivot_index +1, right, k_smallest - left_count - 1)
        
        # def partition(left, right, pivot_index):

        #     pivot_value = nums[pivot_index]

        #     nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        #     store_index = left
        #     for i in range(left, right):
        #         if nums[i] < pivot_value:
        #             nums[store_index], nums[i] = nums[i], nums[store_index]
        #             store_index += 1
            
        #     nums[right], nums[store_index] = nums[store_index], nums[right]

        #     return store_index
    
        # n = len(nums)
        # return quickselect(0,n-1,n-k+1)

# [3,2,1,5,6,4]
# K=2 

# [3,2,1,5,6,4]

# Elements > 4 : [5, 6] -> go to left
# 4: [3,2,1,4] -> go to right

# [5,6, 3,2,1,4]

# current array: [5,6]
# Element > 6: []
# Element <= 


