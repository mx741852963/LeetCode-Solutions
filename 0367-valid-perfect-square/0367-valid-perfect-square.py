class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l <= r:
            mid = (l + r) // 2
            midd = mid * mid
            if midd == num:
                return True
            elif midd > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
# Time O (log n)
# Space O(1)