# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            # base 
            if node == p or node == q or node == None:
                return node
            
            # traversal
            left = dfs(node.left)
            right = dfs(node.right)
            
            # return something
            if left == None:
                return right
            elif right == None:
                return left
            else: 
                return node
        
        return dfs(root)