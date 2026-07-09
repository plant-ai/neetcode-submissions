class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range((n := len(s)) // 2):
            if s[i] != s[n-i-1]:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0 
        right = n - 1

        if self.isPalindrome(s):
            return True

        while left < right:
            l_char = s[left]
            r_char = s[right]
            if l_char == r_char:
                left += 1
                right -= 1
            else:
                if self.isPalindrome(s[left:right]) or self.isPalindrome(s[left+1:right+1]):
                    return True
                else:
                    return False
