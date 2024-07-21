class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mini = min(nums)
        for i in range(n):
            nums[i] -= mini -1
        # Binary Indexed Tree (BIT) Initialization
        maxi = max(nums)
        tr = [0] * (maxi+1)
        re = [] 
        # BIT Query Function
        def count_mi(i):
            c = 0
            while i:
                c += tr[i]
                i -= i & -i
            return c
        # Processing Each Element from Right to Left
        for i in reversed(nums):
            j = i
            while j <= maxi:
                tr[j] += 1
                j += j & -j
            c = count_mi(i-1)
            re.append(c)
        return re[::-1]
