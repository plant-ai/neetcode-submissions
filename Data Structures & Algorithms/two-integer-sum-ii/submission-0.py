class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left = 0 
        right = len(numbers) - 1
        while len(res) < 2:
            num = numbers[left]
            if (num + (num1 := numbers[right])) > target:
                right -= 1
            elif (num + num1) < target:
                left += 1 
            else: 
                res.append(left + 1)
                res.append(right + 1)
        return res



