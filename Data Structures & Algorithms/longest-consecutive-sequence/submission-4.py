class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedNums = sorted(nums)

        longest = 1
        current = 1
        i = 0
        while i < len(sortedNums) - 1:
            diff = sortedNums[i+1] - sortedNums[i]
            if diff == 1:
                current += 1
            elif diff == 0:
                pass  # duplicate, skip without breaking streak
            else:
                current = 1  # streak broken, reset
            longest = max(longest, current)
            i += 1

        return longest