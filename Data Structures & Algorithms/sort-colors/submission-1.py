class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        i = 0
        while i < (n-j):
            if nums[i] == 0:
                nums.insert(0, nums.pop(i))
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums.append(nums.pop(i))
                j += 1
        return nums
        