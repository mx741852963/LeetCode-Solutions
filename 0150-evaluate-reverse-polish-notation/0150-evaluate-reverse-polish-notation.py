class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for num in tokens:
            match num:
                case '+':
                    res.append(res.pop() + res.pop())
                case '*':
                    res.append(res.pop() * res.pop())
                case '-':
                    tem = res.pop()
                    tem_ = res.pop()
                    res.append(int(tem_ - tem))
                case '/':
                    tem = res.pop()
                    tem_ = res.pop()
                    res.append(int(tem_ / tem))
                case _:
                    res.append(int(num))
        return res[-1]
# Time O(n)
# Space O(n)