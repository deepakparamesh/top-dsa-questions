# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
            if root is None:
                return []

            # Dictionary mapping column index -> list of (row, value)
            col_map: defaultdict[int, List[Tuple[int, int]]] = defaultdict(list)

            # BFS queue elements: (node, row, col)
            queue: deque[Tuple[TreeNode, int, int]] = deque()
            queue.append((root, 0, 0))

            # Track horizontal bounds (leftmost & rightmost column indices encountered)
            min_col = max_col = 0

            while queue:
                node, row, col = queue.popleft()

                # Store this node's positional data in its column bucket
                col_map[col].append((row, node.val))

                # Update bounds for later column ordering
                if col < min_col:
                    min_col = col
                if col > max_col:
                    max_col = col

                # Enqueue children with updated coordinates
                # Left child: row+1, col-1
                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                # Right child: row+1, col+1
                if node.right:
                    queue.append((node.right, row + 1, col + 1))

            # Assemble result: iterate from leftmost to rightmost column
            result: List[List[int]] = []
            for col in range(min_col, max_col + 1):
                entries = col_map[col]
                # Sort by row first, then value (Python's tuple sort handles it directly)
                entries.sort(key=lambda pair: (pair[0], pair[1]))
                # Extract just the node values in the sorted order
                column_values = [value for _, value in entries]
                result.append(column_values)

            return result