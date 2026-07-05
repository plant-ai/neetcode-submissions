class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = {}
        longest = 1
        for num in nums:
            if num in numbers:
                numbers[num] += 1
                continue
            numbers[num] = 1
        print(numbers)
        for key in numbers:
            if (key - 1) in numbers:
                continue
            cur_longest = 1
            nxt = key + 1
            while nxt in numbers:
                cur_longest += 1
                nxt += 1
            if cur_longest > longest:
                longest = cur_longest
        return longest