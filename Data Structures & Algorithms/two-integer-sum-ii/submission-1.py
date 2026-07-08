class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        while True:
            num = numbers[left]
            if (num + (num1 := numbers[right])) > target:
                right -= 1
            elif (num + num1) < target:
                left += 1 
            else: 
                return [left + 1, right + 1]


