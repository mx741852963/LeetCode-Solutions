class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        if len(s) < 2: return False 
        for char in s :
            match char :
                case '('|'['|'{' :
                    stack.append(char)
                case _ :
                    if  stack :
                        if char == ')' and stack.pop() != '(' :
                            return False 
                        elif char == ']' and stack.pop() != '[' :
                            return False 
                        elif char == '}' and stack.pop() != '{' :
                            return False 
                    else : 
                        return False 
        return True if not stack else False

                    
