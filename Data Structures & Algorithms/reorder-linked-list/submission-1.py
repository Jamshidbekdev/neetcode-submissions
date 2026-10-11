class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        tmp = second
        prev = None
        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev, tmp = tmp, nxt

        while head and prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2