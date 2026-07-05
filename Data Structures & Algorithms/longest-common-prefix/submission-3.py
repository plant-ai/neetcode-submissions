class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        first_word = strs[0]
        n = len(first_word)
        strings = strs[1:]
        for i in range(n):
            letter = first_word[i]
            for string in strings:
                if (i >= len(string)) or (letter != string[i]):
                    return longest_prefix
            longest_prefix += letter
        return longest_prefix