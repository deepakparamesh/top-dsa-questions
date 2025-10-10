# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# class NestedIterator:
#     def __init__(self, nestedList):
#         """
#         Initialize the iterator with a nested list.
#         We use a stack and reverse the list to process from left to right.
#         """
#         # Stack to store elements (lists or integers) to be processed
#         # We reverse to process in correct order (LIFO nature of stack)
#         self.stack = nestedList[::-1]
    
#     def next(self) -> int:
#         """
#         Returns the next integer in the nested list.
#         Assumes hasNext() is called before next().
#         """
#         # By contract, when next() is called, the top of stack is an integer
#         return self.stack.pop()
    
#     def hasNext(self) -> bool:
#         """
#         Returns True if there are still integers in the nested list.
#         This method does the heavy lifting of unpacking nested lists.
#         """
#         # Keep processing until we find an integer or stack is empty
#         while self.stack:
#             # Peek at the top element
#             top = self.stack[-1]
            
#             # If it's an integer, we're ready for next()
#             if isinstance(top, int):
#                 return True
            
#             # If it's a list, we need to unpack it
#             # Pop the list
#             nested_list = self.stack.pop()
            
#             # Push all elements of the list onto stack (in reverse order)
#             # This handles empty lists naturally (nothing gets pushed)
#             for i in range(len(nested_list) - 1, -1, -1):
#                 self.stack.append(nested_list[i])
        
#         # Stack is empty, no more elements
#         return False
        # while self.stack:

        #     try:
        #         top = next(self.stack[-1])
        #     except StopIteration:
        #         self.stack.pop()
        #         continue
            
        #     if isinstance(top, int):
        #         self.next_integer = top
        #         return True
        #     else:
        #         self.stack.append(iter(top))
            
        # return False
         

# stack [[1,1],2,[1,1]]
#         stack : [2,[1,1]]
#         [1,1]

# [iter([[1,1],2,[1,1]])]
#     [1,1]
#     [iter([2,[1,1]]), iter([1,1])]

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


class NestedIterator:
    def __init__(self, nestedList):
        """
        Initialize the iterator with a nested list.
        We use a stack and reverse the list to process from left to right.
        """
        # Stack to store elements (NestedInteger objects) to be processed
        # We reverse to process in correct order (LIFO nature of stack)
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        """
        Returns the next integer in the nested list.
        Assumes hasNext() is called before next().
        """
        # By contract, when next() is called, the top of stack holds an integer
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        """
        Returns True if there are still integers in the nested list.
        This method does the heavy lifting of unpacking nested lists.
        """
        # Keep processing until we find an integer or stack is empty
        while self.stack:
            # Peek at the top element
            top = self.stack[-1]
            
            # Check if it's an integer using the isInteger() method
            if top.isInteger():
                return True
            
            # If it's a list, we need to unpack it
            # Pop the list
            nested_list = self.stack.pop()
            
            # Get the list using getList() and push elements in reverse order
            list_elements = nested_list.getList()
            
            # Push all elements onto stack (in reverse order for correct processing)
            for i in range(len(list_elements) - 1, -1, -1):
                self.stack.append(list_elements[i])
        
        # Stack is empty, no more elements
        return False