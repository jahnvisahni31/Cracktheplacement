class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr = 0
        buy = 0
        max_pr = 0
        for i in range(1,len(prices)):
            if prices[i-1]>prices[i]:
                max_pr += pr
                buy = i
                pr = 0
            else:
                pr = max(pr,prices[i]-prices[buy])

        return max(max_pr,max_pr+pr)    
            
