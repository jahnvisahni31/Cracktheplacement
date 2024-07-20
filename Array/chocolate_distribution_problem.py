class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        i=0
        j=0
        minim=A[-1]
        while j < N and (i+M-1) < N:
            mini=A[i]
            j=i+M-1
            maxi=A[j]
            minim=min(minim,(maxi-mini))
            i+=1
        return minim
