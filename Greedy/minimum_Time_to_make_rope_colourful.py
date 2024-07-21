class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        sumTime = 0
        curChar = ""
        for c, t in zip(colors, neededTime):
            if c != curChar:
                curChar = c
                curMax = t
            elif t > curMax:
                sumTime += curMax
                curMax = t
            else:
                sumTime += t

        return sumTime
