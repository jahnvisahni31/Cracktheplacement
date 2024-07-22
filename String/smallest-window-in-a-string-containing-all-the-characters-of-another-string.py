
class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        if len(s) < len(p):
            return -1
        
        p_count = [0] * 256  # Assuming ASCII characters
        
        for char in p:
            p_count[ord(char)] += 1
        
        required = len(p)
        formed = 0
        
        window_count = [0] * 256
        
        left, right = 0, 0
        min_length = float('inf')
        start_index = -1
        
        while right < len(s):
            window_count[ord(s[right])] += 1
            
            if window_count[ord(s[right])] <= p_count[ord(s[right])]:
                formed += 1
            
            while formed == required and left <= right:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start_index = left
                
                window_count[ord(s[left])] -= 1
                
                if window_count[ord(s[left])] < p_count[ord(s[left])]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        if start_index == -1:
            return -1
        else:
            return s[start_index:start_index + min_length]
