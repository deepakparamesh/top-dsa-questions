class Solution:
   
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring):
            return substring == substring[::-1]
        """Function to return all possible palindrome partitioning of s."""
        def backtrack(start, path):
            # If we have reached the end of the string, add the current path to the result
            if start == len(s):
                result.append(path[:])
                return

            # Explore all possible partitions
            for end in range(start + 1, len(s) + 1):
                # If the substring s[start:end] is a palindrome, recursively partition the rest
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])  # Choose the palindrome substring
                    backtrack(start + end - start, path)  # Explore further partitions
                    path.pop()  # Undo the choice

        result = []
        backtrack(0, [])
        return result