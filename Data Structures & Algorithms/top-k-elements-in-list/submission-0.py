class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        result = []
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        for _ in range(k):
            count = 0
            index = None
            for i, v in mp.items():
                if v > count:
                    count = v
                    index = i
            result.append(index)
            del mp[index]
        return result