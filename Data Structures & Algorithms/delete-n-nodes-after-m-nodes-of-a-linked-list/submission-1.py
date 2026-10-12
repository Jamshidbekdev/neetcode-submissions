class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        flagM = 1
        inicio = head

        ptr = head

        while ptr != None:
            if flagM:
                for i in range(m - 1):
                    if ptr.next:
                        ptr = ptr.next
                
                flagM = 0
            else:
                aux = ptr
                ptr = ptr.next
                for i in range(n):
                    if ptr:
                        ptr = ptr.next
                
                aux.next = ptr
                flagM = 1
        return inicio