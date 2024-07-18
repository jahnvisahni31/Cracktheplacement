class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ma = 0
        st = []
        for i in range(n+1):
            cu = 0 if i == n else heights[i]
            while st and cu < heights[st[-1]]:
                t = st.pop()
                w = i if not st else i - st[-1]-1
                a = heights[t] * w
                ma = max(ma, a)
            st.append(i)
        return ma
      
