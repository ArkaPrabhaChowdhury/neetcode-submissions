class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = {}
        maxF = 0 
        maxL = 0
        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r],0)
            maxF = max(maxF,seen[s[r]])
            length = r - l + 1
            while r - l + 1 - maxF > k:
                maxF = 0
                seen[s[l]] -=1
                maxF = max(seen.values())
                l+=1
            if length - maxF <= k:
                maxL = max(maxL,length)
                
        return maxL
            
