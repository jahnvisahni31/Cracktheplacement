class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ma = 0
        mi = prices[0]
        for pr in prices:
            mi = min(mi,pr)
            ma = max(ma,pr-mi)
        return ma
