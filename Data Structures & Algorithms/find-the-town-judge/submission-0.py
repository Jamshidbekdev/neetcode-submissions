class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp = defaultdict(int)

        for i, v in trust:
            mp[i] -= 1
            mp[v] += 1

        for i in range(1, n + 1):
            if mp[i] == n - 1:
                return i

        return -1