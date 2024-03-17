# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if node is None:
                return 0
            
            result = 0
            if node.val >= maxVal:
                result = 1
            
            maxVal = max(maxVal, node.val)
            result += dfs(node.left, maxVal)
            result += dfs(node.right, maxVal)
            
            return result
        
        return dfs(root, root.val)