from collections import Counter
class Solution:
    def isValid(self, s: str) -> bool:
        count = Counter(s)
        ss = ')}]'
        lenn= len(s)
        res = []
        if (lenn & 1) == 0 :
            if count['('] == count[')'] and count['['] == count[']'] and count['{'] == count['}']  :
                for i in range(lenn):
                    if s[0]  in ss:
                        break
                    if s[-1] not in ss:
                        break
                    match s[i] :
                        case '('|'{'|'[' :
                            res.append(s[i])
                        case _  :
                            chek = res.pop()
                            match chek:
                                case '(':
                                    if s[i] == ']' or s[i] == '}' :
                                        break
                                    else:
                                        continue
                                case '{':
                                    if s[i] == ']' or s[i] == ')' :
                                        break
                                    else:
                                        continue
                                case '[':
                                    if s[i] == ')' or s[i] == '}' :
                                        break
                                    else:
                                        continue
                if not res and i == lenn - 1 :
                        return True           
        return False