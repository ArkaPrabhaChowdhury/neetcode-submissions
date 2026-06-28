class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            j = 0
            prod=1 
            while j < len(nums):
                if j == i:
                    j+=1
                    continue
                prod = prod*nums[j]
                j+=1
            res.append(prod)
        return res
