class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		n = len(nums)
		t = sorted(nums)
		tr = dict()
		for i in range(n):
		    tr[nums[i]] = i
		sw = 0
		for i in range(n):
		    if nums[i] != t[i]:
		        sw += 1
		        a, b = nums[i], t[i]
		        nums[i],nums[tr[b]] = nums[tr[b]], nums[i]
		        tr[a], tr[b] = tr[b], tr[a]
		return sw
		        
