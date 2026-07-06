from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # O(n) space version
        res = []
        count = Counter(nums)
        threshold = len(nums) // 3
        for key in count:
            if count[key] > threshold:
                res.append(key)
        return res