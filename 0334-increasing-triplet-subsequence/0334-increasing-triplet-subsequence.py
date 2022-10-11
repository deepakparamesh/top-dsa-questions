class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first, second = inf, inf
        
        for third in nums:
            
            if first < second < third: return True
            elif third <= first: first = third
            else: second = third
        
        return False