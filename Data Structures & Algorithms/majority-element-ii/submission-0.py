class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)
        ans = []
        for num in nums:
            mp[num] += 1
        for index, item in mp.items():
            if item > len(nums)//3:
                ans.append(index)
        return ans