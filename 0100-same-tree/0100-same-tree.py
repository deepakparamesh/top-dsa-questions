# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(pNode, qNode):
            if not pNode and not qNode:
                return True
            
            if pNode and qNode and pNode.val == qNode.val:
                leftTraversal = dfs(pNode.left, qNode.left)
                rightTraversal = dfs(pNode.right, qNode.right)
            
                return leftTraversal and rightTraversal
            else: 
                return False
        
        return dfs(p, q)