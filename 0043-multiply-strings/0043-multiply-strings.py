class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)

        res = deque([0] * (m + n))
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                mul_pos, carry_pos = i + j, i + j + 1
                total = mul + res[carry_pos]
                res[carry_pos] = total % 10
                res[mul_pos] += total // 10
        while res[0] == 0:
            res.popleft()
        return "".join(map(str, res))


# Time O(M*N)
# Space O(M+N)
