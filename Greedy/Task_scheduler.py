class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFrequency = [0] * 26
    
        for task in tasks:
            taskFrequency[ord(task) - ord('A')] += 1
    
        maxFrequency = max(taskFrequency)
        maxCount = taskFrequency.count(maxFrequency)
    
        return max((maxFrequency - 1) * (n + 1) + maxCount, len(tasks))
