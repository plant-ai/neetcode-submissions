class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # dict or hash map 
        # need to manage 0s if you have 1, 
        # naive multiplication div route
        zero_pos = []
        n = len(nums)
        c_prod = 1
        for i in range(n):
            if (cur := nums[i]) == 0:
                zero_pos.append(i)
                continue
            c_prod *= cur

        
        if (num_z := len(zero_pos)) == 0:
            return [c_prod // num for num in nums]

        if num_z == 1:
            res = []
            for num in nums:
                if num == 0:
                    res.append(c_prod)
                    continue
                res.append(0)
            return res
        else:
            return [0] * n
            

