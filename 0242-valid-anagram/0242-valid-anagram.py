class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_string_t = "".join(sorted(t))
        sorted_string_s = "".join(sorted(s))
        if sorted_string_t == sorted_string_s :
            return True 
        else:
            return False
        