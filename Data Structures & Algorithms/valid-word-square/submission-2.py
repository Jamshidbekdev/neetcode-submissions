class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        slow = 0
        while slow < len(words):
            fast = 0    # ← changed: start from 0, not from slow
            while fast < len(words[slow]):
                if fast >= len(words) or slow >= len(words[fast]):
                    return False
                if words[slow][fast] != words[fast][slow]:
                    return False
                fast += 1
            slow += 1
        return True