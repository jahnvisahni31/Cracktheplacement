class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        s = 0
        pr = {0:1}
        for i in nums:
            s += i
            if s -k in pr:
                c += pr[s-k]
            if s in pr:
                pr[s] += 1
            else:
                pr[s] = 1
        return c
