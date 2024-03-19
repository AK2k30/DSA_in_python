from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks).values()
        # Find the maximum frequency
        max_freq = max(task_counts)
        # Find the number of tasks that have the maximum frequency
        max_count = list(task_counts).count(max_freq)
        # Calculate the number of partitions, the size of each partition, and the number of idle slots
        part_count = max_freq - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        # Calculate the number of remaining tasks after placing the most frequent ones
        available_tasks = len(tasks) - max_freq * max_count
        # Calculate the number of idle slots after filling in the available tasks
        idles = max(0, empty_slots - available_tasks)
        # The total time is the length of tasks plus the number of idle slots
        return len(tasks) + idles
