class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i in range(len(nums)):
            find = target - nums[i]
            if find in numbers:
                return [numbers[find],i]
            numbers[nums[i]] = i
            