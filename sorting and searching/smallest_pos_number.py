
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        arr.sort()
        c = 1
        for  i in arr:
            if c == i:
                c = c+1
        return c
