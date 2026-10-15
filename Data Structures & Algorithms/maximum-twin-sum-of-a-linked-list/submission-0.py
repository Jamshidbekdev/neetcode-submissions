# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        summ = 0
        while prev:
            summ = max(summ, prev.val + temp.val)
            temp = temp.next
            prev = prev.next
        return summ