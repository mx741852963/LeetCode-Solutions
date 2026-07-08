class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        mod, ans, pow10 = 10**9 + 7, [], [1] * (n + 1)
        prefix = [[0, 0, 0] for _ in range(n + 1)]
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % mod
        for idx, char in enumerate(s):
            digit = int(char)
            if digit == 0:
                prefix[idx + 1][1], prefix[idx + 1][2] = prefix[idx][1], prefix[idx][2]
            else:
                prefix[idx + 1][2], prefix[idx + 1][1] = (
                    prefix[idx][2] + 1,
                    (prefix[idx][1] * 10 + digit) % mod,
                )
            prefix[idx + 1][0] = prefix[idx][0] + digit
        for L, R in queries:
            digit_sum = prefix[R + 1][0] - prefix[L][0]
            if digit_sum == 0:
                ans.append(0)
                continue
            if (k := prefix[R + 1][2] - prefix[L][2]) == 0:
                ans.append(0)
                continue
            sol = (prefix[R + 1][1] - prefix[L][1] * pow10[k]) % mod
            ans.append((digit_sum * sol) % mod)

        return ans
