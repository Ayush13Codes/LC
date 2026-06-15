# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive:
        # T: O(n), S: O(n)
        # Base Case:
        # if not head or not head.next:
        #     return head

        # # Recursive Case:
        # new_head = self.reverseList(head.next)

        # head.next.next = head
        # head.next = None

        # return new_head
        # Iterative:
        # T: O(n), S: O(1)
        c, p = head, None
        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
        return p
