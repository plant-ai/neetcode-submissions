class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        
        if (n := len(strs)) == 0:
            return out


        for i in range(n):
            out = out + strs[i] + "¡"

        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        res = s.split("¡")
        return res[:-1]


