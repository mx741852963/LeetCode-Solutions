class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        mod,ans,pow10 = 10**9 + 7,[],[1] * (n + 1)
        prefix = [[0, 0, 0] for _ in range(n + 1)] 
        for idx, char in enumerate(s):
            digit = int(char)
            p_sum, p_num, p_cnt = prefix[idx]
            is_nz = int(digit != 0)
            prefix[idx + 1] = [p_sum + digit,(p_num * (10**is_nz) + digit) % mod,p_cnt + is_nz]
            pow10[idx+1] = (pow10[idx] * 10) % mod
        for L, R in queries:
            digit_sum=(prefix[R + 1][0] - prefix[L][0])
            if digit_sum == 0 or (k:=prefix[R + 1][2] - prefix[L][2])== 0:
                ans.append(0)
                continue
            sol = (prefix[R + 1][1] - prefix[L][1] * pow10[k]) % mod
            ans.append((digit_sum * sol) % mod)
        return ans
# Time O(n+q)
# Space O(n)
