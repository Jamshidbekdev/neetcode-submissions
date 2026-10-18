# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        ans.sort()
        dummy = ListNode(0)
        curr = dummy
        for num in ans:
            newNode = ListNode(num)
            curr.next = newNode
            curr = curr.next
        return dummy.next