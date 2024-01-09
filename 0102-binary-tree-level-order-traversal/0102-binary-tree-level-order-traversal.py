# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = collections.deque()
        
        if root:
            q.append(root)
        
        while q:
            value = []
            
            for i in range(len(q)):
                node = q.popleft()
                value.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(value)
        
        return result
        
        