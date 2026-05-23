class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for num in operations:
            match num :
                case '+' :
                    res.append(res[-1]+res[-2])
                case 'D':
                    res.append(res[-1] * 2)
                case 'C':
                    res.pop()
                case _ :
                    res.append(int(num))
        return sum(res)
# Time O(n)
# Space O(n)