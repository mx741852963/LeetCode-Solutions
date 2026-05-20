class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = ""
        lenn = len(s)
        for char in s:
            if char.isalpha() or char.isdigit():
                valid += "".join(char)
        valid = valid.lower()
        lenn= len(valid) // 2
        for i in range(lenn):
            if not valid or len(valid) ==1:
                return True
                break
            j = -i - 1
            if valid[i] != valid[j]:
                return False
                break
        return True