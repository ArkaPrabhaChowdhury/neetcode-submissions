class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 =[0] * 26
        freqs2 = [0] * 26
        length = len(s1)
        for s in s1:
            index = ord(s) - ord('a')
            freqs1[index] +=1
        
        l = 0
        for r in range(len(s2)):
            index = ord(s2[r]) - ord('a')
            freqs2[index] +=1
            if freqs1 == freqs2:
                print(freqs1)
                print(freqs2)
                return True
            elif r-l+1 == length and freqs1 != freqs2:
                i = ord(s2[l]) - ord('a')
                freqs2[i] -= 1
                l+=1
        return False