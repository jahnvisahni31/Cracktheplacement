class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            if c == 0:
                ca = i
            if i == ca:
                c += 1
            else:
                c -= 1
        return ca
