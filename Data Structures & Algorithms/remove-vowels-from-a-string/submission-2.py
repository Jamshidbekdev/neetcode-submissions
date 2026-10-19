class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        res = []

        for c in s:
            if c not in vowels:
                res.append(c)

        return "".join(res)