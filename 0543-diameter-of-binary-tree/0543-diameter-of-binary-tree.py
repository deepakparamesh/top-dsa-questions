# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def dfs(node):
            nonlocal maxDiameter
            if node is None:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            
            diameter = leftHeight + rightHeight
            maxDiameter = max(diameter, maxDiameter)
            
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return maxDiameter