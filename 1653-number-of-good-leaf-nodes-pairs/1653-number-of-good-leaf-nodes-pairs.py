# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        
        # good_pairs_count = [0]

        # def dfs(node):

        #     if not node:
        #         return []
            
        #     if not node.left and node.right:
        #         return[1]
            
        #     left_distances = dfs(node.left)
        #     right_distances = dfs(node.right)

        #     for ld in left_distances:
        #         for rd in right_distances:
        #             if ld+rd <= distance:
        #                 good_pairs_count[0] += 1
            
        #     new_distances=[]

        #     for d in left_distances:
        #         if d+1 <= distance:
        #             new_distances.append(d+1)
        #     for d in right_distances:
        #         if d + 1 <= distance:
        #             new_distances.append(d+1)

        #     return new_distances

        # if not root:
        #     return 0

        # dfs(root)

        # return good_pairs_count[0]

        self.count = 0
        
        def dfs(node):
            if not node:
                return []
            
            # If leaf node, return its distance as 0
            if not node.left and not node.right:
                return [1]  # Distance 0 from itself, but will be counted as 1 from parent
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Check all pairs from left and right subtrees
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.count += 1
            
            # Update distances for parent level, incrementing by 1
            return [d+1 for d in left_distances + right_distances if d+1 < distance]
        
        dfs(root)
        return self.count