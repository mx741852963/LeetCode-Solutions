class Solution:
    def maxProduct(self, s: str) -> int:
        maxx = [0]
        n = len(s)
        max_possible = (n // 2) * ((n + 1) // 2)
        def backtrack(i, s1, s2):
            if maxx[0] == max_possible:
                return
            len1, len2 = len(s1), len(s2)
            rem = n - i
            if (len1 + rem) * (len2 + rem) <= maxx[0]:
                return
            if i == n:
                if s1 == s1[::-1] and s2 == s2[::-1]:
                    maxx[0] = max(maxx[0], len1 * len2)
                return
            first, second = (s1, s2) if len1 > len2 else (s2, s1)
            first.append(s[i])
            backtrack(i + 1, s1, s2)
            first.pop()
            if second is not s2 or len1 > 0:
              second.append(s[i])
              backtrack(i + 1, s1, s2)
              second.pop()
            backtrack(i + 1, s1, s2)
        backtrack(0, [], [])
        return maxx[0]
# Time O(n^3+n)
# Space (n)