class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        arr = []
        ba = 0
        for p in points:
            x,y = (p[0] - location[0]), (p[1] - location[1])
            if x == 0 and y == 0:
                ba += 1
                continue
            arr.append(math.degrees(math.atan2(x,y)))
        arr.sort()
        l = len(arr)
        for i in range(l):
            arr.append(arr[i] + 360)
        re = ba
        for i in range(l):
            ind = bisect.bisect_right(arr, arr[i]+angle)
            re = max(re, ind-i+ba)
        return re
