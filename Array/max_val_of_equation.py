class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque()
        res = -float('inf')
        for x, y in points:
            while dq and dq[0][0] < x - k:
                dq.popleft()
            if dq:
                res = max(res, dq[0][1] + y + x)
            while dq and dq[-1][1] <= y - x:
                dq.pop()
            dq.append((x, y - x))
        return res
