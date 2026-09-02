class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0 : return '0'
        org_num = num
        num = abs(num)
        res = []
        while num:
            rem = num % 7
            res.append(str(rem))
            num = num //7
        if org_num < 0 :
            res.append('-')
        return ''.join(res[::-1])
# Time and Space: O(log7 |num|)