class Solution:
    def hammingWeight(self, n: int) -> int:
    #    return Counter(bin(n)[2:])["1"]

# second  sol
        ans = 0
        while n :
            ans+=1
            n = n&(n-1)
        return ans
# Time O(bits)
# Space O(1)