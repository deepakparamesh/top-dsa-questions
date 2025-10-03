class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1] = (char, stack[-1][1] + 1)

                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append((char, 1))
        
        result = []
        for char, count in stack:
            result.append(char * count)
        
        return ''.join(result)



# [(character, count)]
# s= "deeedbbcccbdaa" k = 3

# [('d',2)]
# []

