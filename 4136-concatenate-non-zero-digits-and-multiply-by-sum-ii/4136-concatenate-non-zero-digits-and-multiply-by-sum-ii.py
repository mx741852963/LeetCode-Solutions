class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(s)
        ans = []
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % mod
        pref_sum = [0] * (n + 1)
        pref_num = [0] * (n + 1)
        num_nums = [0] * (n + 1)
        for idx, char in enumerate(s):
            digit = int(char)
            pref_sum[idx + 1] = pref_sum[idx] + digit

            if digit == 0:
                pref_num[idx + 1] = pref_num[idx]
                num_nums[idx + 1] = num_nums[idx]
            else:
                num_nums[idx + 1] = num_nums[idx] + 1
                pref_num[idx + 1] = (pref_num[idx] * 10 + digit) % mod

        for L, R in queries:
            digit_sum = pref_sum[R + 1] - pref_sum[L]
            if digit_sum == 0:
                ans.append(0)
                continue

            k = num_nums[R + 1] - num_nums[L]
            if k == 0:
                ans.append(0)
                continue

            sol = (pref_num[R + 1] - pref_num[L] * pow10[k]) % mod

            ans.append((digit_sum * sol) % mod)

        return ans
