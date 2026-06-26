class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, w = len(board), len(board[0]), len(word)
        def backtrack(r,c, index):
            if board[r][c] != word[index]:
                return False
            if index == w - 1:
                return True
            char = board[r][c]
            board[r][c] = "@"
            for i_, j_ in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dr, dc = r + i_, c + j_
                if 0 <= dr < m and 0 <= dc < n:
                    if backtrack(dr, dc, index + 1):
                        return True
            board[r][c] = char
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
# Time O(n*m*3**w)
# Space O(w)