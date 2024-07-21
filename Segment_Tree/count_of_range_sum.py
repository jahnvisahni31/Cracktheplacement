class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        re = 0
        ls = SortedList()
        ls.add(0)
        for i in range(len(nums)):
            ri = ls.bisect(nums[i]- lower + 0.1)
            le = ls.bisect(nums[i] - upper - 0.1)
            re += ri-le
            ls.add(nums[i])
        return re
