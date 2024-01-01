class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

# #dry run
#         result = [0,0,0,0,0,0,0,0]
        
#         i=0
        
#         stack = [[73,0]]
        
#         i=1
#             while stack and temperatures[i] > stack[-1][0]
#                 result = [1,0,0,0,0,0,0,0]
#                 stack.pop()
            
#             stack = [[74,1]]
#         i=2
            
#             if stack and temperatures[i] > stack[-1][0]
#                 result = [1,1,0,0,0,0,0,0]
#                 stack.pop()
            
#             stack = [[75,2]]
        
#         i=3
#             stack = [[75,2],[71,3]]
#         i=4
#             stack = [[75,2],[71,3],[69,4]]
#         i=5
#             if stack and temperatures[i] > stack[-1][0]
#                 result = [1,1,0,0,1,0,0,0]
#                 stack.pop()
#             stack = stack = [[75,2],[71,3],[72,5]]
#         i=6
#             if stack and temperatures[i] > stack[-1][0]
#                 result = [1,1,0,0,1,1,0,0]
#                 stack.pop()
#             stack = stack = [[75,2],[71,3],[76,6]]
#         i=7
#             if stack and temperatures[i] > stack[-1][0]
#                 result = [1,1,0,0,1,1,0,0]
#                 stack.pop()
#             stack = stack = [[75,2],[71,3],[76,6]]
        
        stack = []
        result = [0] * len(temperatures)
        
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                prevTemp, prevIndex = stack.pop()
                result[prevIndex] = index - prevIndex
            
            stack.append([value, index])
                
        return result
                
#         [73,74,75,71,69,72,76,73]
#              i
        
#         stack=[]
#         result=[0,0,0,0,0,0,0,0]
        
#     i=0
#         stack=[[73,0]]
#     i=1
#         stack=[]
#         []
    
        
        
        