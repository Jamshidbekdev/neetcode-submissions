# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        summ = 0
        result = ListNode()
        data = result
        curr = head
        while curr:
            if curr.val != 0:
                summ += curr.val
            elif summ:
                data.next = ListNode(summ)
                data = data.next
                summ = 0
            curr = curr.next
        return result.next