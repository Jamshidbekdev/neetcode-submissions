# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortLinkedList(self, head: ListNode) -> ListNode:
        prev = head
        curr = head.next
        while curr:
            if curr.val < 0:
                prev.next = curr.next
                curr.next = head
                head = curr
                curr = prev.next
            else:
                prev = prev.next
                curr = curr.next
        return head