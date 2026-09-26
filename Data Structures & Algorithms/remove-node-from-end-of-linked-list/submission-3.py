# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        
        while current is not None:
            length += 1
            current = current.next
        
        if length == n:
            return head.next
        temp = head
        count = 0
        while temp:
            if count == length - n - 1:
                temp.next = temp.next.next
                break
            count += 1
            temp = temp.next
        return head