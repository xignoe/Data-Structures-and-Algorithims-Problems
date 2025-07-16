# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = head
        count = 0

        while a is not None:
            count += 1
            a = a.next

        skipN = count - n

        if skipN == 0:
            return head.next

        b = head
        count = 0

        while b is not None:
            if count == skipN - 1:
                b.next = b.next.next
                break
            else:
                b = b.next
            count += 1

        return head