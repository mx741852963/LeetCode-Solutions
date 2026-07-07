class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        num_fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    num_fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        if num_fresh ==0:
                return 0
        minutes=-1
        while q:
            q_size = len(q)
            minutes+=1
            for _ in range(q_size):
                i,j=q.popleft()
                for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= r < m and 0 <= c < n and grid[r][c]== 1:
                            grid[r][c] = 2
                            num_fresh-=1
                            q.append((r,c))
        if num_fresh ==0:
            return minutes
        else : return -1