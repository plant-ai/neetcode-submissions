

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # O(n) space version
        res = []
        count = {}
        threshold = len(nums) // 3
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key in count:
            if count[key] > threshold:
                res.append(key)
        return res