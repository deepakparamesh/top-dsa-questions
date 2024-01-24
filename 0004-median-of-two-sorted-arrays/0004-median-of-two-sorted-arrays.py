 
#     B = [1,2,3,  4,5,6,7]

#     A = [1,2,  3]
#         L m   R
    
#     total = 10
#     half = 5
    
#     len[BLeft] = half - len[ALeft]
    
#     Cond1: Aleft[rigthMost] <= Bright[leftMost]
#     2 <= 4 
    
#     Cond2: Aright[left] <= Bleft[rigthMost]
#     3 <= 3
#     c
    
#     Find Median
#     if total is odd => min(Bright[leftMost], Aright[leftmost])
#     if total is even =>( max(Aleft[rightmost], Bleft[rightMost]) + min(Bright[leftMost], Aright[leftmost]) ) % 2 => 
    
    # Scenario
#     B = [1,2,  4,4,5,6,7]

#     A = -* [1,2,3] *
#                  l
#                  r
#                  m
    
#     cond1 : True
#     cond2: 2 <= 3 -> True
# O(log(n + m))

# [1,1,2,2,3,3,4,5,6,7] => 3 + 3 % 2 => 3



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        A = nums1
        B = nums2
        
        if len(B) < len(A):
            A , B = B , A
        
        total = len(A) + len(B)
        half = total // 2
        
        left, right = 0, len(A)-1
        
        while True:
            Amid = (left + right) // 2
            Bmid = half - Amid - 2
            
            Aleft = A[Amid] if Amid >=0 else float("-infinity")
            Aright = A[Amid+1] if (Amid + 1) < len(A) else float("infinity")
            Bleft = B[Bmid] if Bmid >=0 else float("-infinity")
            Bright = B[Bmid+1] if (Bmid + 1) < len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = Amid - 1
            elif Aleft < Bright:
                left = Amid + 1
        
                
        
        
        
        