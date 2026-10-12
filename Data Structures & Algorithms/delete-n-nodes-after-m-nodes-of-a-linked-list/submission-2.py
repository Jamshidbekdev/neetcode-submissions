# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = head
        while curr:
            for _ in range(m - 1):
                if curr.next:
                    curr = curr.next
                else:
                    break
            target = curr.next
            for _ in range(n):
                if target:
                    target = target.next
            curr.next = target
            curr = target
        return head

