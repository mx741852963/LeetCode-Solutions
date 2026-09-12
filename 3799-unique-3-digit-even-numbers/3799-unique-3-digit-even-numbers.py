class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        sol, n = [], len(digits)
        visited = set()
        digits.sort()

        def backtrack(count):
            curr_len = len(sol)
            if curr_len == 3:
                return count + 1
            for i in range(n):
                if i in visited:
                    continue
                if i > 0 and digits[i] == digits[i - 1] and (i - 1) not in visited:
                    continue
                if curr_len == 0 and digits[i] == 0:
                    continue
                if curr_len == 2 and (digits[i] & 1):
                    continue
                visited.add(i)
                sol.append(digits[i])
                count = backtrack(count)
                sol.pop()
                visited.remove(i)
            return count

        return backtrack(0)
# Time O(n**3) : n * n - 1 * n -2
# Space O(n) : sort func