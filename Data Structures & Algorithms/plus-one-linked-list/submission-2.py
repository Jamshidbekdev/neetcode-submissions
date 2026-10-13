# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        temp = head
        reversedListNode = self.reverseListNodes(temp)
        curr = reversedListNode
        carry = 1
        prev = None
        while curr:
            if carry: 
                val = curr.val + carry
                curr.val = val % 10
                carry = val // 10
            prev = curr
            curr = curr.next
        if carry:
            prev.next = ListNode(carry)
            return self.reverseListNodes(reversedListNode)
        return self.reverseListNodes(reversedListNode)
        # 1 -> 2 -> 3 -> 4
        # 4 -> 3 -> 2 -> 1

    def reverseListNodes(self, curr: ListNode) -> ListNode:
        temp = curr
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev, temp = temp, nxt
        return prev