class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
            
        while l <= r:
            m = (l + r) // 2
                
            if nums[m] == target:
                return m  # Target found, return index
            elif nums[m] < target:
                l = m + 1  # Target is in the right half
            else:
                r = m - 1  # Target is in the left half
                    
        return -1  # Target not found