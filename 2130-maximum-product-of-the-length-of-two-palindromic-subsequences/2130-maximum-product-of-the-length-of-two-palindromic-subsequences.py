class Solution:
    def maxProduct(self, s: str) -> int:
        maxx = [0]
        n  =len(s)
        def backtrack(i , s1,s2):
            if i ==n:
                str1 = "".join(s1)
                str2 = "".join(s2)
                if str1 == str1[::-1 ]and str2 == str2[::-1 ]:
                    maxx[0] = max(maxx[0],len(str1)*len(str2)) 
                return 
            s1.append(s[i])
            backtrack(i + 1, s1, s2)
            s1.pop() 
            s2.append(s[i])
            backtrack(i + 1, s1, s2)
            s2.pop()  
            backtrack(i + 1, s1, s2)
        backtrack(0, [], [])
        return maxx[0]