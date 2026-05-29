class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1,len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        wight_of_s1 = [0]*26
        wight_of_s2 = [0]*26
        for i in range(len1):
            wight_of_s1[ord(s1[i])-97] +=1
            wight_of_s2[ord(s2[i])-97] +=1
        if wight_of_s1==wight_of_s2:
                return True
        for r in range(len1, len2):
            wight_of_s2[ord(s2[r])-97] +=1
            wight_of_s2[ord(s2[r-len1])-97] -=1 
            if wight_of_s1==wight_of_s2:
                return True
        return False
# Time O(n)
# Space O(1)