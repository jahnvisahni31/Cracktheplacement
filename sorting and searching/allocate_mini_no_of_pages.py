class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        #code here
        beg = max(arr)
        end = sum(arr) 
        ans =  0 
        while beg <= end:
            mid  = (beg + end) // 2
            # distribution
            c = 1
            p =  0
            for i in range(n):
                p  += arr[i]
                if p  > mid:
                    c +=1
                    p = arr[i]
                    # break
            if c <= m:
                # for checking the diffrences betweeen the students
                ans = mid 
                end  = mid - 1
            else:
                beg = mid + 1
        if m > n:
            return -1
        else:
            
            return ans
