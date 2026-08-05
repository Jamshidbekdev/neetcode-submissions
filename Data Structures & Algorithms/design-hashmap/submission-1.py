class MyHashMap:

    def __init__(self):
        self.length = 1000
        self.hashMaps = [[]*i for i in range(self.length)]

    def put(self, key: int, value: int) -> None:
        ind = key % self.length
        print(value)
        for index, (k, v) in enumerate(self.hashMaps[ind]):
            if k == key:
                self.hashMaps[ind][index] = (key, value)
                return None
        self.hashMaps[ind].append((key, value))
        return None

    def get(self, key: int) -> int:
        ind = key % self.length
        for index, (k, value) in enumerate(self.hashMaps[ind]):
            if k == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        ind = key % self.length
        for index, (k, value) in enumerate(self.hashMaps[ind]):
            if k == key:
                self.hashMaps[ind].pop(index)
        return None

#   [      
#     ind0 => [
#         0 => (0, 3), 1 => (5, 6)
#     ],
#     1 => [
#         (1, 7), (6, 16)
#     ],
#     ....
#   ]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)