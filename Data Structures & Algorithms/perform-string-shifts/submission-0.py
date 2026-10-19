class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = sum(amount if direction == 1 else -amount for direction, amount in shift)
        total_shift %= len(s)
        return s[-total_shift:] + s[:-total_shift]