class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range((n := len(s)) // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
