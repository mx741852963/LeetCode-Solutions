class Solution:
    def maxProduct(self, n: int) -> int:
        ans = []
        while n :
            ans.append(n%10)
            n = n //10
        ans.sort()
        return ans[-1]*ans[-2]
# Time O(n log n)
# Space O(n)