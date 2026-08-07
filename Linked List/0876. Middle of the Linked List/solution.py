from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

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

# Find the middle node
middle_node = solution.middleNode(node1)

# Print the value of the middle node
if middle_node:
    print("Middle node value:", middle_node.val)



    