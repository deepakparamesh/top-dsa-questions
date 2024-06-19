class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Initialize a stack to keep track of current path lengths
        stack = []
        # Variable to store the maximum path length
        max_length = 0

        # Split the input by newline characters to get each file/directory entry
        entries = input.split('\n')

        for entry in entries:
            # Count the number of tab characters to determine the depth
            depth = entry.count('\t')
            # Remove the tab characters to get the actual name
            name = entry.replace('\t', '')

            # Pop from stack to go back to the correct depth
            while len(stack) > depth:
                stack.pop()

            # Calculate the current length
            if stack:
                current_length = stack[-1] + len(name) + 1  # Add 1 for the '/' separator
            else:
                current_length = len(name)

            # If it's a file, update the maximum length
            if '.' in name:
                max_length = max(max_length, current_length)
            else:
                # If it's a directory, push the current length onto the stack
                stack.append(current_length)

        return max_length