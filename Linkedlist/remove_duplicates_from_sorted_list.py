# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cu = head
        while cu and cu.next:
            if cu.val == cu.next.val:
                cu.next = cu.next.next
            else:
                cu = cu.next
        return head
