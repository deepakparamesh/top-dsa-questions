# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        # Traverse the tree to find insertion position
        current = root
        while True:
            # If value is less than current node, go left
            if val < current.val:
                # If left child exists, move to it
                if current.left:
                    current = current.left
                else:
                    # Found insertion position, insert and break
                    current.left = TreeNode(val)
                    break
            # If value is greater than current node, go right
            else:
                # If right child exists, move to it
                if current.right:
                    current = current.right
                else:
                    # Found insertion position, insert and break
                    current.right = TreeNode(val)
                    break
        
        return root