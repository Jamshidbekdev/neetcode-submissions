# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length, current = 0, head
        while current:
            length += 1
            current = current.next
        dummy = ListNode(0)
        dummy.next = head
        width = 1
        while width < length:
            tail, current = dummy, dummy.next
            while current:
                left, left_count = current, 0
                for _ in range(width):
                    if current is None: break
                    left_count += 1
                    current = current.next
                right, right_count = current, 0
                for _ in range(width):
                    if current is None: break
                    right_count += 1
                    current = current.next
                while left_count or right_count:
                    if right_count == 0 or (left_count and left.val <= right.val):
                        chosen, left = left, left.next
                        left_count -= 1
                    else:
                        chosen, right = right, right.next
                        right_count -= 1
                    tail.next = chosen
                    tail = chosen
                tail.next = current
            width *= 2
        return dummy.next