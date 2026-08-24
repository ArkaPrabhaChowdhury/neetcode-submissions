class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # store count of each character with char mapping in hashmaps and compare

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        if countS == countT:
            return True
        else:
            return False