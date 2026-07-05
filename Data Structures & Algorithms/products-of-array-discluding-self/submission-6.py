
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      res = []
      left = []
      right = []
      n = len(nums)
      l, r = 1, 1
      for i in range(n):
         left.append(l)
         l *= nums[i]
         right = [r] + right
         r *= nums[n-i-1]

      return [num1 * num2 for num1, num2 in zip(left, right)]

