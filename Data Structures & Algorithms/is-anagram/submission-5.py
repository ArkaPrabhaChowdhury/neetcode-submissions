class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_text_s = "".join(sorted(s))
        sorted_text_t = "".join(sorted(t))

        if sorted_text_s == sorted_text_t:
            return True
        return False