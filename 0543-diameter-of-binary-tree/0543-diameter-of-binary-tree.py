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
            
            # base condition
            if not node:
                return 0
            
            # traversal
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            
            # core logic calculation
            currentNodeDiameter = leftHeight + rightHeight
            maxDiameter = max(maxDiameter, currentNodeDiameter)
            
            # recursive function return
            height = 1 + max(leftHeight, rightHeight)
            return height

        dfs(root)
        return maxDiameter