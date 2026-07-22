# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head 
        fast = head 

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                    
                return slow

        return None
    

# node creation 
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# node connection
node1.next = node2
node2.next = node3
node3.next = node4

# create cycle 
node4.next = node2

#head of linked list 

head = node1

solution = Solution()

res = solution.detectCycle(head)

if res:
    print("Cycle starts at ",res.val)

else:
    print(None)
