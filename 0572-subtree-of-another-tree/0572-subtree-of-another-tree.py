# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(main, sub):
            if not main:
                return False
            
            if main.val == sub.val:
                if isSameTree(main, sub):
                    return True
            
            leftTraversal = dfs(main.left, sub)
            rightTraversal = dfs(main.right, sub)
            return leftTraversal or rightTraversal
        
        def isSameTree( main, sub):
            if not main and not sub:
                return True
            if main and sub and main.val == sub.val:
                leftTraverse = isSameTree(main.left, sub.left)
                rightTraverse = isSameTree(main.right, sub.right)    
                return leftTraverse and rightTraverse
            else:
                return False
            
        return dfs(root, subRoot)