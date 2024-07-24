class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(nums, mid):
            ways = 1
            subarrSum = 0
            for i in range(len(nums)):
                if subarrSum + nums[i] <= mid:
                    subarrSum += nums[i]
                else:
                    ways += 1
                    subarrSum = nums[i]
            return ways

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low+high) // 2
            if helper(nums, mid) > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
      
