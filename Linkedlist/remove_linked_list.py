# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        pr, cu = d, head
        while cu:
            if cu.val == val:
                pr.next = cu.next
            else:
                pr = cu
            cu = cu.next
        return d.next
