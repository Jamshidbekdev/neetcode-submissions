class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = {}
        for v in text:
            mp[v] = mp.get(v, 0) + 1
        
        return min(
            mp.get('b', 0),
            mp.get('a', 0),
            mp.get('l', 0) // 2,
            mp.get('o', 0) // 2,
            mp.get('n', 0)
        )