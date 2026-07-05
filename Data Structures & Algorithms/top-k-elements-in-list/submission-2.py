class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        dic_2 = {}
        res = []
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1 
        print(dic)
        for key in dic:
            value = dic[key]
            print(key, value)
            dic_2.setdefault(value, []).append(key)
        i = len(nums)  
        while k > 0:
            if i in dic_2:
                val = dic_2[i]
                for num in val:
                    k -= 1
                    res.append(num)
            i -= 1

        return res