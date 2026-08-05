class MyHashMap:

    def __init__(self):
        self.bucketSize = 1000
        self.buckets = [[]*i for i in range(self.bucketSize)]

    def put(self, key: int, value: int) -> None:
        index = key % self.bucketSize
        for i, (iKey, item) in enumerate(self.buckets[index]):
            if iKey == key:
                self.buckets[index][i] = (key, value)
                return None
        self.buckets[index].append((key, value))
        return None

    def get(self, key: int) -> int:
        index = key % self.bucketSize
        for i, (iKey, item) in enumerate(self.buckets[index]):
            if iKey == key:
                return item
        return -1

    def remove(self, key: int) -> None:
        index = key % self.bucketSize
        for i, (iKey, item) in enumerate(self.buckets[index]):
            if iKey == key:
                self.buckets[index].pop(i)
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)