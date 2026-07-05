class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        threshold = n // 2
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        for key in dic:
            if dic[key] > threshold:
                return key