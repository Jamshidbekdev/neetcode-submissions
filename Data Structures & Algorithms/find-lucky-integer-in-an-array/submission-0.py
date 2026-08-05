class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = {}
        for v in arr:
            mp[v] = mp.get(v, 0) + 1  # Corrected dictionary key assignment
        
        max_lucky = -1
        for val, freq in mp.items():
            if val == freq:
                max_lucky = max(max_lucky, val)  # Track the maximum lucky number
                
        return max_lucky