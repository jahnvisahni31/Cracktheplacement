#User function Template for python3


class Solution:
    def hello(self,heights):
        stack=[]
        maxA=0
        for index,height in enumerate(heights):
            start=index
            while stack and stack[-1][1]>height:
                i,h=stack.pop()
                maxA=max(maxA,h*(index-i))
                start=i
            stack.append([start,height])

        for i,h in stack:
            maxA=max(maxA,h*(len(heights)-i))
        return maxA
        
    def maxArea(self,M, n, m):
        # code here
        maxArea=0
        h = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if M[i][j]==1:
                    h[j]+=1
                else:
                    h[j]=0
            maxArea=max(maxArea,self.hello(h))
        return maxArea
                    
