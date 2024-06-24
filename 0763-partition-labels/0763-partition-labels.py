class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}  # Hash table to track last occurrence of each char
        for i, char in enumerate(s):
            last_occurrence[char] = i

        result = []
        start, max_index = 0, 0
        for i, char in enumerate(s):
            max_index = max(max_index, last_occurrence[char])
            if i == max_index:
                result.append(i - start + 1)  # Partition length
                start = i + 1  # Start of the next partition
        return result