class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += str(len(string)) + "#" + string
        return out

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # read digits until the '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])      # everything from i up to '#'
            i = j + 1                 # step past the '#' onto content
            res.append(s[i:i+length]) # grab exactly `length` chars
            i += length               # step past the content
        return res
