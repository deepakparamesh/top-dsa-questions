# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_sum = 0
        # Stack stores tuples of (node, current_number)
        stack = [(root, 0)]
        
        while stack:
            node, current_number = stack.pop()
            
            # Build the number for current path
            current_number = current_number * 10 + node.val
            
            # If leaf node, add to total sum
            if not node.left and not node.right:
                total_sum += current_number
            
            # Add children to stack for further processing
            if node.right:
                stack.append((node.right, current_number))
            if node.left:
                stack.append((node.left, current_number))
        
        return total_sum