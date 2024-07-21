class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums.sort()
        su1 = 0
        l = len(nums)
        for i in range(l):
            j = i+1
            k = l-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        an = list(s)
        return an
      
