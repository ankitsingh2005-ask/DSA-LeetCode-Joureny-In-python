from typing import Optional
# Definition for singly-linked list.
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None
        if left == right:
            return head

        t = head
        before = None
        pos = 1

        while t is not None:
            if pos < left:
                before = t
                t = t.next
                pos += 1
                continue

            # Reverse the sublist from left to right
            curr = t
            prev = None
            times = right - left + 1
            while times > 0 and curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                times -= 1

            t.nest = curr
            if before:
                before.next = prev
                return head

            return prev

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
# Reverse the linked list between positions 2 and 4
reversed_head = solution.reverseBetween(node1, 2, 4)

# Print the modified linked list
current = reversed_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next       




        
        