class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = ""
        lenn = len(s)
        valid = "".join([char.lower() for char in s if char.isalnum()])
        lenn= len(valid) // 2
        for i in range(lenn):
            if not valid or len(valid) ==1:
                return True
            j = -i - 1
            if valid[i] != valid[j]:
                return False
        return True