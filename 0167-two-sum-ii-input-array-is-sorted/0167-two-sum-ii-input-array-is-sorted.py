class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         prevMap = {}  # val -> index

#         for i, n in enumerate(numbers):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff]+1, i+1]
#             prevMap[n] = i
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]