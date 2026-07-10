class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = 0
        j = 0
        res = ""
        while (flag := (i < n)) and (j < m):
            res += (word1[i] + word2[j])
            i += 1
            j += 1
        if not flag:
            return res + word2[j:]
        return res + word1[i:]
            

        