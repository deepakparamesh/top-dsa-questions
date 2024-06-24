class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
    
        end = float('-inf')
        remove_count = 0

        for interval in intervals:
            if interval[0] >= end:
                # No overlap, update the end to the end of the current interval
                end = interval[1]
            else:
                # Overlap, increment the remove count
                remove_count += 1

        return remove_count