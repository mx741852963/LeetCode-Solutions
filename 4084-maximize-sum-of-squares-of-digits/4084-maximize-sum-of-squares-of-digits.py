class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = '9' * (sum//9)
        sum %= 9 
        if sum : ans += str(sum)
        n = len(ans)
        if n > num : return ""
        ans += "0"*(num-n)
        return ans
    # Time O(num)
    # space O(1)