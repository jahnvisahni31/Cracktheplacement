# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
MOD = 10**9+7
class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        cur1 = first
        cur2 = second
        res = ''
        res1 = ''
        while cur1:
            res += str(cur1.data)
            cur1 = cur1.next
        while cur2:
            res1 += str(cur2.data)
            cur2 = cur2.next
        a1 = int(res)
        a2 = int(res1)
        return a1 * a2 % MOD
