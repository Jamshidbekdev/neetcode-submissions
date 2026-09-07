class TimeMap:

    def __init__(self):
        self.mapp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapp:
            self.mapp[key] = [(value, timestamp)]
        else:
            self.mapp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapp:
            return ""
        nums = self.mapp[key]
        l, r = 0, len(nums) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            if timestamp >= nums[mid][1]:
                result = nums[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return result

    # {
    #     'alice': [('happy', 1), ('sad', 3), ('something', 4), ('good', 6)]
    # }