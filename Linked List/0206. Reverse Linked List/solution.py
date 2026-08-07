from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next  # Store the next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev to current node
            curr = next_node  # Move to the next node

        return prev  # Return the new head of the reversed list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#-------------------main program----------------------
# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Create an instance of the Solution class
solution = Solution()

# Reverse the linked list
reversed_head = solution.reverseList(node1) 
print("Reversed linked list:")
# Print the reversed linked list    
current = reversed_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")   

    