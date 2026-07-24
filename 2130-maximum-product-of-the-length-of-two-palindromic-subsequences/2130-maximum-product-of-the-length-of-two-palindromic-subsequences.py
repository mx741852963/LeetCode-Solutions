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
            s1.append(s[i])
            backtrack(i + 1, s1, s2)
            s1.pop()

            s2.append(s[i])
            backtrack(i + 1, s1, s2)
            s2.pop()
            backtrack(i + 1, s1, s2)

        backtrack(0, [], [])
        return maxx[0]
