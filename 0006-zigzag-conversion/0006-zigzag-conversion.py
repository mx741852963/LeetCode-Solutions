class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        if n ==1: return s
        i =0 
        d = 1
        rows = [[]for _ in range(n)]
        for char in s :
            rows[i].append(char)
            if i == 0 :
                d= 1
            elif i == n-1:
                d = -1
            i +=d
        res = ""
        for j in range(n):
            res +="".join(rows[j])
        return res