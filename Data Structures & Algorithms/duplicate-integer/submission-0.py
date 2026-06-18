class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = set(nums)
        if len(dupSet) == len(nums):
            return False
        else:
            return True