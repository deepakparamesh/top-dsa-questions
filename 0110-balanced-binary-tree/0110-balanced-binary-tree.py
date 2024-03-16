# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
                return [True, 0]
            
            
            left = dfs(node.left)
            right = dfs(node.right)
            height = 1 + max(left[1], right[1])
            
            isBalanced = abs(left[1] - right[1]) <= 1 and (left[0] and right[0])
            return [isBalanced, height]
            
        return dfs(root)[0]
        