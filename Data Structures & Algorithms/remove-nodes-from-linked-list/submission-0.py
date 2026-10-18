# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        new_head = prev
        curr = new_head
        prev = None
        max_val = 0
        while curr:
            if curr.val < max_val:
                prev.next = curr.next
            else:
                max_val = curr.val
                prev = curr
            curr = curr.next

        # Reverse back to original order
        curr = new_head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        return prev