class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return (f:=cache(lambda amount,i:int(amount==0) or amount>0 and i<len(coins) and f(amount-coins[i],i)+f(amount,i+1)))(amount,0)
