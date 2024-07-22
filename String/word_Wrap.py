
class Solution:
	def solveWordWrap(self, nums, k):
		#Code here
		def solve(i,rem):
		    if i==n:
		        return 0
		    
		    if dp[i][rem]!=-1:
		        return dp[i][rem]
		        
		    if nums[i]>rem:
		              
		        ans = (rem+1)*(rem+1)+solve(i+1,k-nums[i]-1)
		    
		    else:
		        opt1 = (rem+1)*(rem+1)+solve(i+1,k-nums[i]-1)
		        opt2 = solve(i+1,rem-nums[i]-1)
		        ans = min(opt1,opt2)
		    
		    dp[i][rem]=ans
		    return dp[i][rem]

		n = len(nums)
		dp = [[-1]*(k+1) for i in range(n+1)]
		return solve(0,k)

