class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        dp = {}
        for mask in range(1, 1 << n):
              sub = ""
              for i in range(n):
                if (mask >> i) & 1:
                  sub += s[i]
              if sub == sub[::-1]:
                dp[mask] = len(sub)

        max_prod = 0
        for m1, l1 in dp.items():
          for m2, l2 in dp.items():
            if not (m1 & m2): 
              if l1 * l2 > max_prod:
                max_prod = l1 * l2
    
        return max_prod
        # maxx = [0]
        # n = len(s)

        # def backtrack(i, s1, s2):
        #     len1, len2 = len(s1), len(s2)
        #     rem = n - i
        #     if (len1 + rem) * (len2 + rem) <= maxx[0]:
        #         return
        #     if i == n:
        #         if s1 == s1[::-1] and s2 == s2[::-1]:
        #             maxx[0] = max(maxx[0], len1 * len2)
        #         return
        #     s1.append(s[i])
        #     backtrack(i + 1, s1, s2)
        #     s1.pop()

        #     s2.append(s[i])
        #     backtrack(i + 1, s1, s2)
        #     s2.pop()
        #     backtrack(i + 1, s1, s2)

        # backtrack(0, [], [])
        # return maxx[0]
