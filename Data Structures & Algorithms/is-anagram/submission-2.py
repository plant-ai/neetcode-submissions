class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_s = {}
        for char in s:
            counts_s[char] = counts_s.get(char, 0) + 1
        print(counts_s)
        for char in t:
            if char in counts_s:
                counts_s[char] -= 1
                if counts_s.get(char) < 0:
                    return False
            else:
                return False
        return True