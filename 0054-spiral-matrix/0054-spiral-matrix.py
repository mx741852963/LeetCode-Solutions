class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        j = 0

        while len(ans) < m * n:
            for i in range(j, n - j):
                if len(ans) < m * n:
                    ans.append(matrix[j][i])
            for i in range(1 + j, m - j):
                if len(ans) < m * n:
                     ans.append(matrix[i][-1 - j])
            for i in range(n - 2 - j, j - 1, -1):
                if len(ans) < m * n:
                    ans.append(matrix[-1 - j][i])
            for i in range(m - 2 - j, j, -1):
                if len(ans) < m * n: ans.append(matrix[i][j])

            j += 1
        return ans

        
        