class Solution:
    def grayCode(self, n: int) -> List[int]:
        sol = [0]
        visited = {0}
        target_size = 1 << n 
        def backtrack():
            if len(sol) == target_size:
                last =sol[-1]
                if (last & (last - 1)) == 0:
                    return True 
                return False
            cur = sol[-1]
            for i in range(n):
                mask = 1 << i
                next_num = cur ^ mask
                if next_num not in visited:
                    visited.add(next_num)
                    sol.append(next_num)
                    if backtrack(): return True
                    sol.pop()
                    visited.remove(next_num)
        backtrack()
        return sol