class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        result = []  # Store intersection intervals
        i = j = 0    # Two pointers for the two lists
        
        # Continue while both pointers are within bounds
        while i < len(firstList) and j < len(secondList):
            
            # Get current intervals from both lists
            interval_a = firstList[i]   # [start_a, end_a]
            interval_b = secondList[j]  # [start_b, end_b]
            
            # Calculate potential intersection boundaries
            # Intersection start: latest start time of both intervals
            intersection_start = max(interval_a[0], interval_b[0])
            
            # Intersection end: earliest end time of both intervals  
            intersection_end = min(interval_a[1], interval_b[1])
            
            # Check if intersection exists (start <= end means valid interval)
            if intersection_start <= intersection_end:
                # Valid intersection found - add to result
                result.append([intersection_start, intersection_end])
            
            # Advance pointer strategy: move the pointer of interval that ends first
            # This interval cannot intersect with any future intervals in other list
            if interval_a[1] <= interval_b[1]:
                # First interval ends first (or both end at same time)
                i += 1
            else:
                # Second interval ends first
                j += 1
        
        return result