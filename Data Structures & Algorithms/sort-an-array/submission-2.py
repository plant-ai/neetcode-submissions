class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if (n := len(nums)) <= 0:
            return nums
        mid = self.median_of_three(nums, 0, n-1)
        pivot = nums[mid]
        del nums[mid]
        left_half = [x for x in nums if x < pivot]
        right_half = [x for x in nums if x >= pivot]
        return self.sortArray(left_half) + [pivot] + self.sortArray(right_half) 

    def median_of_three(self, nums, lo, hi):
        mid = (lo + hi) // 2
        if nums[lo] > nums[mid]:
            nums[lo], nums[mid] = nums[mid], nums[lo]
        if nums[lo] > nums[hi]:
            nums[lo], nums[hi] = nums[hi], nums[lo]
        if nums[mid] > nums[hi]:
            nums[mid], nums[hi] = nums[hi], nums[mid]
        return mid 
