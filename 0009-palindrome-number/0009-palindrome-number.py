class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        j = n-1
        for i in range(n):
            if s[i] != s[j] :
                 return False
            j-=1
            if j==i : break
            
        return True