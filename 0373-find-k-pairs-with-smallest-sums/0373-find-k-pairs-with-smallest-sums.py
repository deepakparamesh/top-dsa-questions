class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        
        result = []
        min_heap = []
        
        # Initialize heap with pairs from first element of nums1 with all elements of nums2
        # But limit to min(k, len(nums2)) to avoid unnecessary elements
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))
        
        while min_heap and len(result) < k:
            curr_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # Only add the next element from nums1 (moving down)
            # This ensures we don't add duplicates
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return result