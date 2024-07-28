#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        if not head or not head.next:
            return head

        # Count the occurrences of 0, 1, and 2
        count_0 = count_1 = count_2 = 0
        current = head
        while current:
            if current.data == 0:
                count_0 += 1
            elif current.data == 1:
                count_1 += 1
            else:
                count_2 += 1
            current = current.next

        # Update the values in the linked list based on counts
        current = head
        while current:
            if count_0 > 0:
                current.data = 0
                count_0 -= 1
            elif count_1 > 0:
                current.data = 1
                count_1 -= 1
            else:
                current.data = 2
                count_2 -= 1
            current = current.next

        return head
    
