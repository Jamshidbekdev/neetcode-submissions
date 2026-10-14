# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        rl1 = self.reverseNodes(l1)
        rl2 = self.reverseNodes(l2)
        temp = result
        carry = 0
        while rl1 or rl2 or carry:
            val1 = rl1.val if rl1 else 0 
            val2 = rl2.val if rl2 else 0
            val  = val1 + val2 + carry
            carry = val // 10
            temp.next = ListNode(val % 10)
            rl1 = rl1.next if rl1 else None
            rl2 = rl2.next if rl2 else None
            temp = temp.next
        return self.reverseNodes(result.next)
    def reverseNodes(self, curr: ListNode) -> ListNode:
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        return prev