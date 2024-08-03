#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        #Your code here
        def reverse(head):
            prev=None
            curr=None
            while head:
                curr=head
                head=head.next
                curr.next=prev
                prev=curr
            return curr
        head=reverse(head)
        m=0
        Max=None
        curr=None
        prev=None
        while head:
            if head.data>=m:
                curr=head
                head=head.next
                m=curr.data
                curr.next=Max
                Max=curr
            else:
                head=head.next
        if curr.data>=m:
            return curr
        else:
            return Max
