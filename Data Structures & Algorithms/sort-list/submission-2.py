# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        first = self.sortList(head)
        second = self.sortList(second)
        result = ListNode(0)
        data = result
        while first and second:
            if first.val < second.val:
                data.next = first
                first = first.next
            else:
                data.next = second
                second = second.next
            data = data.next
        data.next = first if first else second
        return result.next