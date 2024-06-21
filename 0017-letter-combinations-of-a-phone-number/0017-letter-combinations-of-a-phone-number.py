class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        if not digits:
            return []

        # Helper function for recursion
        def backtrack(index, path):
            # If the current path is complete (equal to the length of digits)
            if index == len(digits):
                combinations.append("".join(path))
                return

            # Get the letters that the current digit maps to
            possible_letters = digit_to_letter[digits[index]]
            for letter in possible_letters:
                path.append(letter)  # Choose a letter
                backtrack(index + 1, path)  # Recur for the next digit
                path.pop()  # Undo the choice

        combinations = []
        backtrack(0, [])
        return combinations