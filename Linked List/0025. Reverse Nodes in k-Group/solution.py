

from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, left, times):
        prev = None
        curr = left

        while times > 0:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            times -= 1

        return prev, curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None:
            return head

        left = head
        res = None
        prevleft = None
        right = None
        size = k

        while left:

            # Check whether k nodes are available
            right = left
            size = k

            while size > 0 and right:
                right = right.next
                size -= 1

            # Less than k nodes remain
            if size > 0:
                if prevleft:
                    prevleft.next = left
                else:
                    res = left
                break

            times = k

            # Reverse k nodes
            right, nextleft = self.reverse(left, times)

            if prevleft:
                prevleft.next = right
            else:
                res = right

            prevleft = left
            left = nextleft

        return res


# ------------------- main program ----------------------

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

# Create Solution object
sol = Solution()

# Set k
k = 3

# Call function
res = sol.reverseKGroup(node1, k)

# Print result
while res:
    print(res.val, end=" ")
    res = res.next

