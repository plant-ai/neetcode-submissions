class Solution:
    def anagram_tuple(self, string):
        arr = [0] * 26
        if string == "":
            return tuple(arr)
        for letter in string:
            pos = ord(letter) - ord("a")
            arr[pos] += 1
        return tuple(arr)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            tup26 = self.anagram_tuple(string)
            if tup26 not in dic:
                dic[tup26] = []
            dic[tup26].append(string)
        return list(dic.values())

