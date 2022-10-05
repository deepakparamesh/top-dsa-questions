# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def h(node,ans):
            if(node):
                ans-=node.val
            else:
                return None
            if(ans==0 and (node.left==node.right==None)):
                return True
            else:
                return h(node.left,ans) or h(node.right,ans)
        return h(root,targetSum)