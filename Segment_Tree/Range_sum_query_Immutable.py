Seclass NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        n = 0
        for i in range(left, right+1):
            n = n + self.nums[i]
        return n
