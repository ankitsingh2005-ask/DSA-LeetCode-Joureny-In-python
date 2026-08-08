
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Helper function to reverse a sublist of the linked list
    def reverse(self, left, times):
        prev = None
        curr = left

        while times > 0 and curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            times -= 1

        return prev, curr

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None

        size = 0
        res = None
        left = head
        prevleft = None
        right = None

        # Calculate size
        while left:
            size += 1
            left = left.next

        left = head

        while left:

            # If only one node is left
            if left.next == None:
                if prevleft:
                    prevleft.next = left
                else:
                    res = left
                break

            times = 2

            # Reverse two nodes
            right, left.next = self.reverse(left, times)

            # Connect previous pair to current pair
            if prevleft:
                prevleft.next = right
            else:
                res = right

            # Move prevleft to the last node
            # of the current reversed pair
            prevleft = left

            # Move to next pair
            left = left.next

        return res


# ------------------- main program -------------------

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

# Create solution object
sol = Solution()

# Swap pairs
res = sol.swapPairs(node1)

# Print result
while res:
    print(res.val, end=" ")
    res = res.next
