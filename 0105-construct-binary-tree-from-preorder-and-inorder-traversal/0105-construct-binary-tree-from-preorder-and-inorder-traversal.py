# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
        
        preorder_index = 0
        
        def array_to_tree(left, right):
            nonlocal preorder_index
            
            if left > right:
                return None
            
            root_value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_value)
            
            root.left = array_to_tree(left, inorder_index_map[root_value]-1)
            root.right = array_to_tree(inorder_index_map[root_value]+1, right)
            
            return root
        
        return array_to_tree(0, len(inorder)-1)
    

    
# pre-order => root -> left -> right
# in-order => left -> root -> right
# root = 3

# [9,3, 15,20,7]

