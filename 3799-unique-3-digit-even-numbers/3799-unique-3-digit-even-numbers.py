class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        self.ans, sol, n = 0, [], len(digits)
        visited = set()
        digits.sort()
        def backtrack():
            if len(sol) == 3:
                if sol[0] != 0 and not sol[2] & 1:
                    self.ans += 1
                return
            for i in range(n):
                if i in visited:
                    continue
                if i > 0 and digits[i] == digits[i - 1] and (i - 1) not in visited:
                    continue
                visited.add(i)
                sol.append(digits[i])
                backtrack()
                sol.pop()
                visited.remove(i)

        backtrack()
        return self.ans
