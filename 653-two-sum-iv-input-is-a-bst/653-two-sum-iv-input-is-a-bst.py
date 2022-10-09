# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        self.inOrder(root, nums)
        
        for i in range(len(nums)):
            if k - nums[i] in nums[i+1:]:
                return True
        
        return False
        
        
    
    def inOrder(self, root, nums):
        if root == None:
            return
        self.inOrder(root.left, nums)
        nums.append(root.val)
        self.inOrder(root.right, nums)
        
        
        