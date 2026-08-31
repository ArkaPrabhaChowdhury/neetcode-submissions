class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        start = end = 0
        maxLength = 0

        while end < len(s):
            while s[end] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[end])
            length = len(seen)
            maxLength = max(length,maxLength)
            end+=1
        
        return maxLength
