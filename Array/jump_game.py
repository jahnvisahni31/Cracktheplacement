class Solution:
    def canJump(self, nums: List[int]) -> bool:
        f = 0
        i = 0
        while i <= f and i < len(nums):
            f = max(f, i + nums[i])
            i += 1
        return f >= len(nums) - 1
