class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 2:
            return min(height[0], height[1])
        water = 0
        l = 0
        r = n - 1
        while l < r:
            curr_water = min(height[r], height[l]) * (r - l)
            water= max(water,curr_water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water
