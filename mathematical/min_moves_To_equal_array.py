class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mi = len(nums)
        m = nums[mi//2]
        c = 0
        for n in nums:
            c += abs(m-n)
        return c
