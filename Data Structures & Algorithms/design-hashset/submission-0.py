class MyHashSet:

    def __init__(self):
        self.buckets = []

    def add(self, key: int) -> None:
        for item in self.buckets:
            if item == key:
                return None
        self.buckets.append(key)
        return None;

    def remove(self, key: int) -> None:
        for index, item in enumerate(self.buckets):
            if item == key:
                self.buckets.pop(index)
                return None
        return None;

    def contains(self, key: int) -> bool:
        for item in self.buckets:
            if item == key:
                return True
        return False;


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)