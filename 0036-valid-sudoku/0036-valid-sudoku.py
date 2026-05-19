class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lenn = len(board)
        flag = True
        d = 0
        m, n = 0, 0
        for i in board:
            if not flag:
                break
            seen = set()
            for digit in i:
                if digit == ".":
                    continue
                if digit not in seen:
                    seen.add(digit)
                else:
                    flag = False
                    break
        i = 0
        while i < 9:
            if not flag:
                break
            seen = set()
            for k in range(9):
                digit = board[k][i]
                if digit == ".":
                    continue
                if digit not in seen:
                    seen.add(digit)
                else:
                    flag = False
                    break
            i += 1
        while d < 9:
            if not flag:
                break
            seen = set()
            for i in range(m, 3 + m):
                for j in range(n, 3 + n):
                    digit = board[i][j]
                    if digit == ".":
                        continue
                    if digit not in seen:
                        seen.add(digit)
                    else:
                        flag = False
                        break
            if n < 6:
                n += 3
            else:
                n = 0
                m += 3
            d += 1
        return flag
