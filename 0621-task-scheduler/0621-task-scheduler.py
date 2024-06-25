class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_freq_count = list(task_counts.values()).count(max_freq)

        intervals = (max_freq - 1) * (n + 1) + max_freq_count
        return max(len(tasks), intervals)