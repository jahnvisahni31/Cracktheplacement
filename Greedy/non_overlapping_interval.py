class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        c, pre = 0, intervals[0]
        for i in intervals[1:]:
            if pre[1]>i[0]: c+=1
            else: pre=i
        return c
