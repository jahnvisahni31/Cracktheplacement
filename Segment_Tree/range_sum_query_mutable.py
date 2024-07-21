class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.t = [0]* 2 *  self.n
        for i in range(self.n):
            self.t[i + self.n] = nums[i]
        for i in range(self.n-1, 0 ,-1):
            self.t[i] = self.t[2*i] + self.t[2*i+1]
        print(self.t)
    def update(self, index: int, val: int) -> None:
        index += self.n
        self.t[index] = val
        while index > 1:
            self.t[index//2] = self.t[index] + self.t[index^1]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        r = 0
        while left <= right:
            if left & 1:
                r += self.t[left]
                left += 1
            if right & 1 == 0:
                r += self.t[right]
                right -= 1
            left //= 2
            right //= 2
        return r
        
