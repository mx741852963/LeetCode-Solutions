class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    b_idx = (r // 3) * 3 + (c // 3)
                    boxes[b_idx].add(val)

        def backtrack(row ,col) :
            if col == 9:
                row += 1
                col = 0
            if row == 9:
                return True

            if board[row][col] != '.':
                return backtrack(row, col + 1)

            b_idx = (row // 3) * 3 + (col // 3)

            for num in range(1, 10):
                char = str(num)
                

                if (char not in rows[row]) and (char not in cols[col]) and (char not in boxes[b_idx]):
                    

                    board[row][col] = char
                    rows[row].add(char)
                    cols[col].add(char)
                    boxes[b_idx].add(char)
                    
                    if backtrack(row, col + 1):
                        return True
                    

                    board[row][col] = '.'
                    rows[row].remove(char)
                    cols[col].remove(char)
                    boxes[b_idx].remove(char)

            return False

        backtrack(0, 0)

# Time and Space O(1)
