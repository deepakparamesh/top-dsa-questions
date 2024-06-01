class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()  # store maximum values
        min_queue = deque()  # store minimum values

        left = 0

        for n in nums:
            # Maintain the max_queue in decreasing order of elements
            while max_queue and n > max_queue[-1]:
                max_queue.pop()
            max_queue.append(n)

            # Maintain the min_queue in increasing order of elements
            while min_queue and n < min_queue[-1]:
                min_queue.pop()
            min_queue.append(n)

            # If the absolute difference between the maximum and minimum elements
            # in the current window exceeds the limit, remove one element
            # from either or both queues and increment the left pointer
            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1

        return len(nums) - left