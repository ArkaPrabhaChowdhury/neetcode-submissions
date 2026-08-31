class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        tMap = {}
        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)
            
        sMap = {}
        valid = 0
        
        # Track the best window: (window_length, start_index)
        min_len = float("inf")
        res_start = 0
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in tMap:
                sMap[char] = 1 + sMap.get(char, 0)
                if sMap[char] == tMap[char]:
                    valid += 1
            
            # Shrink window from the left as long as it contains all chars of t
            while valid == len(tMap):
                # 1. Record the current valid window if it's smaller
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res_start = l
                
                # 2. Pop s[l] from the window map
                left_char = s[l]
                if left_char in tMap:
                    if sMap[left_char] == tMap[left_char]:
                        valid -= 1
                    sMap[left_char] -= 1
                
                # 3. Move left pointer
                l += 1
                
        return "" if min_len == float("inf") else s[res_start : res_start + min_len]