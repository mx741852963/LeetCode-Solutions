class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for num in tokens:
            match num:
                case '+':
                    tem = res.pop()
                    tem_ = res.pop()
                    res.append(int(tem_ + tem))
                case '*':
                    tem = res.pop()
                    tem_ = res.pop()
                    res.append(int(tem_ * tem))
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