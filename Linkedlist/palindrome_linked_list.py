# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ic = []
        cu = head
        while cu:
            ic.append(cu.val)
            cu = cu.next
        
        le , ri = 0, len(ic)-1
        while le < ri:
            if ic[le] != ic[ri]:
                return False
            le += 1
            ri -= 1
        return True
