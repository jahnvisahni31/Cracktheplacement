class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for nu in range(len(nums)):
            if nums[nu] != 0 and nums[i] == 0:
                nums[i] = nums[nu]
                nums[nu] = 0
                i += 1
            elif nums[i] != 0:
                i += 1
