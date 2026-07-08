class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = (''.join([char for char in s if char.isalnum()])).lower()
        for i in range ((n := len(cleaned)) // 2):
            if cleaned[i] != cleaned[n - i - 1]:
                print(cleaned[i], cleaned[n-i-1])
                return False
        return True