class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        answer = []
        result = [[] for i in range(len(nums) + 1)]
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        for index, value in mp.items():
            result[value].append(index)
        count = 0
        for index in range(len(result) - 1, 0, -1):
            for val in result[index]:
                if count < k:
                    answer.append(val)
                    count += 1
        return answer
