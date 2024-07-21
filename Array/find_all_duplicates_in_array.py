class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return
        re = []
        i = 0
        while i < n:
            if nums[i] == i+1:
                i += 1
                continue
            index = nums[i]-1
            if nums[index] == index+1:
                re.append(nums[i])
                i += 1
            else:
                tmp = nums[i]
                nums[i] = nums[index]
                nums[index] = tmp
                if index < i:
                    i += 1
        return re
