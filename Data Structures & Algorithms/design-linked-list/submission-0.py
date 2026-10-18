class MyLinkedList:

    def __init__(self):
       self.lists = [] 

    def get(self, index: int) -> int:
        if 0 <= index < len(self.lists):
            return self.lists[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.lists = [val] + self.lists

    def addAtTail(self, val: int) -> None:
        self.lists.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= len(self.lists):
            self.lists.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.lists):
            del self.lists[index]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)