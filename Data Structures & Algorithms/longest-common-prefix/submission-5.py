class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        first_word = strs[0]
        for i in range(len(first_word)):
            letter = first_word[i]
            for string in strs[1:]:
                if i >= len(string) or letter != string[i]:
                    return longest
            longest += letter 
        return longest     
                    

        