# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        
        q = deque()
        
        q.append(root)
        
        while q:
            localArray = []
            for index in range(len(q)):
                currentNode = q.popleft()
                localArray.append(currentNode.val)
                if currentNode.left:
                    q.append(currentNode.left)
                if currentNode.right:
                    q.append(currentNode.right)
            result.append(localArray)
        
        return result
                
            
        
        