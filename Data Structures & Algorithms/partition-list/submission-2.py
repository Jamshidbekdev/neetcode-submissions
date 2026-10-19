# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        result = ListNode(0)
        data = ListNode(0, head)
        prev = data
        dummy = result
        curr = head
        while curr:
            if curr.val < x:
                dummy.next = ListNode(curr.val)
                dummy = dummy.next
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        if data.next:
            dummy.next = data.next
        return result.next