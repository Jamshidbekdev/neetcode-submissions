class TimeMap:

    def __init__(self):
        self.mapp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapp:
            self.mapp[key].append((timestamp, value))
        else:
            self.mapp[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapp:
            return ""
        l, r = 0, len(self.mapp[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if self.mapp[key][mid][0] <= timestamp:
                res = self.mapp[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
