class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}
        for i , nu in enumerate(nums):
            if target - nu in p:
                return [i, p[target-nu]]
            p[nu] = i
