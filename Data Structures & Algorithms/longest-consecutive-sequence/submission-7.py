class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length=0
        for n in nums:
            if n-1 not in numSet:
                count = 1
                while n+count in numSet:
                    count+=1
                length = max(count,length)
        
        return length

        