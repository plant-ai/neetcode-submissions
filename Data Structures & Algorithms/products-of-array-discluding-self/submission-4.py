from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       left = []
       right = nums[1:]
       res = []
       n = len(nums)
       for num in nums:
        res.append(math.prod((combined := left + right)))
        left.append(num)
        if len(right) > 0:
            right.pop(0)

       return res
