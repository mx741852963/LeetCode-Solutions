class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        p_c = [0] * (n + 1)
        for c in citations:
            p_c[min(c, n)] += 1
        h = n
        p = p_c[n]
        while p < h:
            h -= 1
            p += p_c[h]
        return h


# Time O(n)
# Spcae O(n)
