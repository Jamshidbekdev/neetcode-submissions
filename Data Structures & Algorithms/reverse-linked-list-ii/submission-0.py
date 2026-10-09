# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = self.findNodeByPosition(dummy, left)
        group_next = group_prev
        for _ in range(right - left + 1):
            group_next = group_next.next
        temp = group_prev.next
        curr = temp
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        group_prev.next = prev
        temp.next = curr
        return dummy.next

    def findNodeByPosition(self, node: Optional[ListNode], position: int):
        while position > 1:
            node = node.next
            position -= 1
        return node