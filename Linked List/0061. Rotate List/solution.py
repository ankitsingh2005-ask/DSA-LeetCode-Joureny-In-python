from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        last = head 
        n = 1
        res = None

        while last.next is not None:
            n += 1
            last = last.next

        k = k % n
        if k == 0:
            return head

        count = 1
        t = head

        while t:
            if count == (n-k):
                break
            count += 1
            t = t.next

        last.next = head
        res = t.next
        t.next = None

        return res

#------------------main program----------------

#create Node 
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# connection in node

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Head of linked list
head = node1

# k
k = 2

# Create Solution object
sol = Solution()

# Call function
res = sol.rotateRight(head, k)

# Print result
current = res

while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")